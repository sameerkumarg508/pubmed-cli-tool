import argparse
import csv
from typing import List, Union
from Bio import Entrez, Medline

Entrez.email = "sameerkumarg508@gmail.com"

# ---------- Step 1: Fetch Metadata from PubMed ----------
def fetch_pubmed_metadata(pubmed_ids: List[str]) -> List[dict]:
    handle = Entrez.efetch(db="pubmed", id=pubmed_ids, rettype="medline", retmode="text")
    records = list(Medline.parse(handle))
    return records

# ---------- Step 2: Search PubMed IDs based on query ----------
def search_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    return record["IdList"]

# ---------- Step 3: Filter Company Affiliations ----------
def is_non_academic(affiliations: Union[str, List[str]]) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "hospital", "department", "centre"]

    if isinstance(affiliations, list):
        return any(not any(word in affil.lower() for word in academic_keywords) for affil in affiliations)
    elif isinstance(affiliations, str):
        return not any(word in affiliations.lower() for word in academic_keywords)
    else:
        return False

# ---------- Step 4: Main Program ----------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed with company-affiliated authors.")
    parser.add_argument("--query", type=str, required=True, help="Search query for PubMed")
    parser.add_argument("--file", type=str, default=None, help="CSV filename to save results")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    # Step 1: Get PubMed IDs for the query
    if args.debug:
        print(f"🔍 Searching PubMed for: '{args.query}'")
    pubmed_ids = search_pubmed_ids(args.query)

    if args.debug:
        print(f"✅ Found {len(pubmed_ids)} IDs:", pubmed_ids)

    # Step 2: Fetch metadata
    papers = fetch_pubmed_metadata(pubmed_ids)

    # Step 3: Decide output mode
    output_to_file = args.file is not None
    if output_to_file:
        f = open(args.file, mode="w", newline='', encoding="utf-8")
        writer = csv.writer(f)
        writer.writerow([
            "PubmedID",
            "Title",
            "Publication Date",
            "Non-academic Author(s)",
            "Company Affiliation(s)",
            "Corresponding Author Email"
        ])

    for paper in papers:
        pmid = paper.get("PMID", "N/A")
        title = paper.get("TI", "N/A")
        date = paper.get("DP", "N/A")
        authors = paper.get("FAU", [])
        affiliations = paper.get("AD", [])
        emails = paper.get("AID", [])

        if is_non_academic(affiliations):
            authors_str = ", ".join(authors)
            affil_str = ", ".join(affiliations) if isinstance(affiliations, list) else affiliations
            email_str = ", ".join([e for e in emails if "@" in e]) if emails else "N/A"

            if output_to_file:
                writer.writerow([pmid, title, date, authors_str, affil_str, email_str])
            else:
                print("\n--- Paper ---")
                print(f"PMID: {pmid}")
                print(f"Title: {title}")
                print(f"Date: {date}")
                print(f"Authors: {authors_str}")
                print(f"Affiliations: {affil_str}")
                print(f"Emails: {email_str}")

            if args.debug:
                print(f"✔️ Processed paper with PMID {pmid}")

    if output_to_file:
        f.close()
        print(f"\n✅ Results saved to {args.file}")
