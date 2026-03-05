#!/usr/bin/env python3
import argparse
import sys
import os
from datetime import date

def generate_latex_template(title, subtitle, disease_state, doc_type):
    content = r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.5in]{geometry}
\usepackage{tcolorbox}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{booktabs}

\title{""" + title + r"""}
\author{Clinical Decision Support System}
\date{\today}

\begin{document}

\maketitle
\thispagestyle{empty}

% Report Information Box
\begin{tcolorbox}[colback=blue!5!white, colframe=blue!75!black, title=Report Information]
\textbf{Document Type:} """ + doc_type + r"""\\
\textbf{Disease State:} """ + disease_state + r"""\\
\textbf{Subtitle:} """ + subtitle + r"""\\
\textbf{Analysis Date:} \today
\end{tcolorbox}

\vspace{0.3cm}

% Key Finding #1: Primary Results
\begin{tcolorbox}[colback=blue!5!white, colframe=blue!75!black, title=Primary Efficacy Results]
\begin{itemize}
    \item [Primary finding placeholder]
    \item [Statistical summary placeholder]
\end{itemize}
\end{tcolorbox}

\vspace{0.3cm}

% Key Finding #2: Biomarker Insights
\begin{tcolorbox}[colback=green!5!white, colframe=green!75!black, title=Biomarker Stratification Findings]
\begin{itemize}
    \item [Molecular subtype insight placeholder]
    \item [Biomarker association placeholder]
\end{itemize}
\end{tcolorbox}

\vspace{0.3cm}

% Key Finding #3: Clinical Implications
\begin{tcolorbox}[colback=orange!5!white, colframe=orange!75!black, title=Clinical Recommendations]
\begin{itemize}
    \item [Actionable recommendation placeholder]
    \item [GRADE grading placeholder]
\end{itemize}
\end{tcolorbox}

\newpage
\tableofcontents
\newpage

\section{Introduction}
[Detail the clinical context and target population]

\section{Methods}
[Detail statistical analysis, biomarker assays, and patient selection]

\section{Results}
[Detailed findings with tables and figures]

\section{Discussion}
[Interpretation of findings and comparison with existing evidence]

\section{Recommendations}
[Detailed clinical guidance and decision algorithms]

\end{document}
"""
    return content

def main():
    parser = argparse.ArgumentParser(description='Initialize a Clinical Decision Support (CDS) LaTeX document.')
    parser.add_argument('--title', default='Evidence-Based Clinical Decision Support', help='Document title')
    parser.add_argument('--subtitle', default='Cohort Analysis and Recommendations', help='Document subtitle')
    parser.add_argument('--disease', default='Unspecified Condition', help='Disease state')
    parser.add_argument('--type', choices=['Cohort Analysis', 'Treatment Guidelines'], default='Cohort Analysis', help='Document type')
    parser.add_argument('--output', default='cds_document.tex', help='Output LaTeX file name')

    args = parser.parse_args()

    content = generate_latex_template(args.title, args.subtitle, args.disease, args.type)
    
    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"Generated LaTeX template: {args.output}")
    print("MANDATORY: Page 1 contains the executive summary. Do not move it.")

if __name__ == "__main__":
    main()
