#!/usr/bin/env python3
"""
Driver script for Petri Net containment checking.
This script demonstrates how to use the Verifier and GenReport classes
to perform containment analysis and generate reports.
"""

from sfc import SFC
from sfc_verifier import Verifier
from genreport import GenReport


def check_pn_containment_html( verifier, gen_report, sfc1, pn1, sfc2, pn2):
    gen_report.sfc_to_dot(sfc1, "sfc1.dot")
    gen_report.dot_to_png("sfc1.dot", "sfc1.png")
    gen_report.petrinet_to_dot(pn1, "pn1.dot")
    gen_report.dot_to_png("pn1.dot", "pn1.png")
    gen_report.sfc_to_dot(sfc2, "sfc2.dot")
    gen_report.dot_to_png("sfc2.dot", "sfc2.png")
    gen_report.petrinet_to_dot(pn2, "pn2.dot")
    gen_report.dot_to_png("pn2.dot", "pn2.png")

    # Prepare image paths for report
    img_paths = {
        "sfc1": gen_report.img_to_base64("sfc1.png"),
        "pn1": gen_report.img_to_base64("pn1.png"),
        "sfc2": gen_report.img_to_base64("sfc2.png"),
        "pn2": gen_report.img_to_base64("pn2.png")
    }
    
    # Use GenReport instance to generate HTML report
    return gen_report.generate_containment_html_report(
        verifier.cutpoints1, verifier.cutpoints2, verifier.paths1, verifier.paths2, 
        verifier.matches1, verifier.unmatched1, verifier.contained, img_paths
    )


def main():
    """Main driver function for Petri Net containment analysis."""
    # Create verifier and report generator instances
    verifier = Verifier()
    gen_report = GenReport()
    
    # Load SFC models
    sfc1 = SFC()
    sfc2 = SFC()
    sfc1.load("dec2hex.txt")
    sfc2.load("dec2hex_mod.txt")
    
    # Convert SFC models to Petri nets
    pn1 = sfc1.to_pn()
    pn2 = sfc2.to_pn()
    # Perform containment analysis
    verifier.check_pn_containment(sfc1, pn1, sfc2, pn2)

    # Generate HTML report
    html_report = check_pn_containment_html(verifier, gen_report, sfc1, pn1, sfc2, pn2)
    json_report = gen_report.generate_containment_json_report(
        verifier.cutpoints1, verifier.cutpoints2, verifier.paths1, verifier.paths2, 
        verifier.matches1, verifier.unmatched1, verifier.contained
    )
    # Write report to file
    with open("pn_containment_report.html", "w") as f:
        f.write(html_report)
    print("HTML report written to pn_containment_report.html")
    with open("pn_containment_report.json", "w") as f:
        f.write(json_report)
    # Demonstrate access to analysis results
    print(f"Model 1 contained in Model 2: {verifier.is_contained()}")
    print(f"Number of unmatched paths: {len(verifier.get_unmatched_paths())}")
    print(f"Number of matched paths: {len(verifier.get_matched_paths())}")

if __name__ == "__main__":
    main()
