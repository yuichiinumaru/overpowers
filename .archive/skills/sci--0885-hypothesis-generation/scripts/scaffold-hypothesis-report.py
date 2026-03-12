#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scaffold a scientific hypothesis report (LaTeX).")
    parser.add_argument("title", help="Title of the research report")
    parser.add_argument("--output", "-o", default="hypothesis_report.tex", help="Output .tex file name")
    args = parser.parse_args()

    template = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{tcolorbox}
\usepackage{xcolor}
\usepackage{natbib}
\usepackage{titlesec}

% Mock style package environments if .sty is missing
\newtcolorbox{summarybox}[1][]{colback=blue!5!white,colframe=blue!75!black,title={#1}}
\newtcolorbox{hypothesisbox1}[1][]{colback=blue!5!white,colframe=blue!75!black,title={#1}}
\newtcolorbox{predictionbox}[1][]{colback=amber!5!white,colframe=amber!75!black,title={#1}}

\title{""" + args.title + r"""}
\author{Hypothesis Generation Skill}
\date{\today}

\begin{document}

\maketitle

\begin{summarybox}[Executive Summary]
Brief overview of the phenomenon and the proposed hypotheses.
\end{summarybox}

\section{Competing Hypotheses}

\newpage
\begin{hypothesisbox1}[Hypothesis 1: Mechanistic Title]
\textbf{Mechanistic Explanation:} 
Explain HOW and WHY here (6-10 sentences).

\textbf{Key Supporting Evidence:}
\begin{itemize}
    \item Evidence point 1 \citep{author2023}
    \item Evidence point 2
\end{itemize}

\textbf{Core Assumptions:}
\begin{itemize}
    \item Assumption 1
\end{itemize}
\end{hypothesisbox1}

\section{Testable Predictions}

\begin{predictionbox}[Key Predictions]
\begin{itemize}
    \item If H1 is true, we expect to see...
\end{itemize}
\end{predictionbox}

\appendix
\section{Comprehensive Literature Review}
Detailed literature search results and synthesis.

\section{Detailed Experimental Designs}
Full protocols for testing the hypotheses.

\bibliographystyle{plainnat}
\begin{thebibliography}{99}
\bibitem[Author(2023)]{author2023} Author, A. (2023). Title of the paper. \textit{Journal Name}.
\end{thebibliography}

\end{document}
"""

    with open(args.output, "w") as f:
        f.write(template)

    print(f"Generated LaTeX hypothesis report scaffold: {args.output}")
    print("Compile with: xelatex " + args.output)

if __name__ == "__main__":
    main()
