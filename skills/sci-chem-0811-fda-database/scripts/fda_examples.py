from fda_query import FDAQuery
import json

def main():
    fda = FDAQuery()
    
    print("--- 1. Drug Adverse Events for Metformin ---")
    events = fda.query_drug_events("metformin", limit=2)
    if "results" in events:
        for i, res in enumerate(events["results"]):
            reactions = [r["reactionmeddrapt"] for r in res.get("patient", {}).get("reaction", [])]
            print(f"Report {i+1} Reactions: {', '.join(reactions)}")
    
    print("\n--- 2. Top Reactions for Aspirin ---")
    reactions = fda.count_by_field(
        "drug", "event",
        search="patient.drug.medicinalproduct:aspirin",
        field="patient.reaction.reactionmeddrapt"
    )
    if "results" in reactions:
        for res in reactions["results"][:5]:
            print(f"{res['term']}: {res['count']}")

    print("\n--- 3. Device Recalls for 'pacemaker' ---")
    device_recalls = fda.query("device", "enforcement", 
                              search="product_description:pacemaker", 
                              limit=2)
    if "results" in device_recalls:
        for res in device_recalls["results"]:
            print(f"Recall: {res.get('product_description')[:100]}...")
            print(f"Reason: {res.get('reason_for_recall')[:100]}...")

    print("\n--- 4. Food Recalls for 'listeria' ---")
    food_recalls = fda.query_food_recalls(reason="listeria", classification="I")
    if "results" in food_recalls:
        print(f"Found {len(food_recalls['results'])} Class I listeria recalls (limited)")
        for res in food_recalls["results"][:2]:
            print(f"Product: {res.get('product_description')[:100]}...")

    print("\n--- 5. Substance Lookup: Acetaminophen ---")
    substance = fda.query_substance_by_name("acetaminophen")
    if "results" in substance:
        res = substance["results"][0]
        print(f"UNII: {res.get('unii')}")
        print(f"Molecular Formula: {res.get('molecularFormula')}")

if __name__ == "__main__":
    main()
