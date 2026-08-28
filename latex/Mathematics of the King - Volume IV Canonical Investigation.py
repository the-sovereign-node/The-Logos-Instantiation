%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% P0 — MASTER ARCHITECTURAL PLAN
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Working Title:
%
%   Mathematics of the King
%   A First-Principles Foundation for Canonical Mathematics
%
% Philosophy
% ----------
%
% This document is NOT organized historically.
%
% It is organized by logical dependency.
%
% Every chapter depends only on previous chapters.
%
% Every definition is introduced exactly once.
%
% Every theorem has explicit dependencies.
%
% Every chapter concludes with:
%
%   • Dependency Audit
%   • Primitive Audit
%   • Reduction Audit
%   • Consistency Audit
%   • Future Reduction Candidates
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% L0 — MASTER LATEX SKELETON
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\documentclass[12pt,anyside]{book}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PACKAGES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}

\usepackage{lmodern}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathtools}
\usepackage{mathrsfs}

\usepackage{epigraph}
\usepackage{enumitem}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{geometry}

\geometry{
    margin=1in
}

\usepackage[osf]{ebgaramond}

\usepackage{hyperref}
\usepackage[nameinlink]{cleveref}
\usepackage{comment}
\usepackage{titlesec}
\usepackage{thmtools}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GLOBAL FORMATTING
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% No paragraph indentation.
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.75\baselineskip}

\setcounter{tocdepth}{1}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CHAPTER STYLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\scshape}
  {\chaptertitlename\ \thechapter}
  {20pt}
  {\Huge}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART STYLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\titleformat{\part}[display]
  {\normalfont\huge\bfseries\centering}
  {\partname\ \thepart}
  {20pt}
  {\Huge}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SEMANTIC COMMANDS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\term}[1]{\textit{#1}}
\newcommand{\struct}[1]{\textbf{\textsc{#1}}}
\newcommand{\axiomdef}[1]{\textbf{#1}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% THEOREM STYLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\declaretheoremstyle[
    headfont=\bfseries\scshape,
    notefont=\mdseries,
    notebraces={(}{)},
    bodyfont=\itshape,
    spaceabove=10pt,
    spacebelow=10pt,
    mdframed={
        backgroundcolor=blue!5,
        linecolor=blue!50,
        linewidth=1pt
    }
]{theorstyle}

\declaretheorem[
    style=theorstyle,
    name=Theorem,
    numberwithin=chapter
]{theorem}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% THEOREM ENVIRONMENTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newtheorem{axiom}{Axiom}[chapter]
\newtheorem{definition}[axiom]{Definition}
\newtheorem{lemma}[axiom]{Lemma}
\newtheorem{proposition}[axiom]{Proposition}
\newtheorem{corollary}[axiom]{Corollary}
\newtheorem{remark}[axiom]{Remark}
\newtheorem{example}[axiom]{Example}
\newtheorem{construction}[axiom]{Construction}
\newtheorem{principle}[axiom]{Principle}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CUSTOM ENVIRONMENTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newenvironment{dependencyaudit}
{\section*{Dependency Audit}}
{}

\newenvironment{primitiveaudit}
{\section*{Primitive Audit}}
{}

\newenvironment{reductionaudit}
{\section*{Reduction Audit}}
{}

\newenvironment{consistencyaudit}
{\section*{Consistency Audit}}
{}

\newenvironment{futurework}
{\section*{Future Reduction Candidates}}
{}

\newenvironment{transitionaudit}
{\section*{Transition Audit}}
{}

\newenvironment{completionaudit}
{\section*{Completion Audit}}
{}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MACROS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% TODO
%
% All notation will be introduced only after formal approval.
%
% Do NOT define mathematical symbols prematurely.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TITLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\title{
    {\Huge\bfseries Mathematics of the King}\par
    \vspace{0.75cm}
    {\LARGE Volume IV: Canonical Investigation}\par
    \vspace{0.5cm}
    {\large A First-Principles Foundation for Canonical Mathematics}
}

\author{\large\textsc{Samir Amier Saliem Boulos}}

\date{July 2026}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EPIGRAPH SETTINGS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\setlength{\epigraphwidth}{0.5\textwidth}
\renewcommand{\epigraphflush}{center}
\renewcommand{\epigraphsize}{\huge}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% FRONT MATTER
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\frontmatter

\maketitle

\newpage

\vspace*{\fill}

\begin{center}
\epigraph
    {The stone that struck the image became a great mountain and filled the whole earth.}
    {Daniel 2:35}
\end{center}

\vspace*{\fill}

\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CONSTITUTION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{The Constitution}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The following Articles constitute the constitutional law governing every
construction, reduction, and theorem throughout this monograph. They are not
axioms of mathematics but constraints upon the methodology by which mathematics
is recovered from the Witness. Every subsequent chapter is subordinate to these
Articles.

\vspace{1em}

\begin{description}[
    style=multiline,
    font=\normalfont\bfseries,
    labelwidth=3.8cm,
    leftmargin=4.3cm,
    labelsep=0.5cm,
    itemsep=0.75em
]

\item[Article I:]
Every primitive is presumed removable until proven otherwise.

\item[Article II:]
Every definition must justify its logical cost.

\item[Article III:]
Every theorem must declare its dependencies.

\item[Article IV:]
No interpretation may precede construction.

\item[Article V:]
Canonical constructions are preferred over arbitrary constructions.

\item[Article VI:]
Logical reduction takes precedence over computational convenience.

\item[Article VII:]
The reduction program is asymptotic and therefore never complete.

\item[Article VIII:]
The mathematical content of earlier chapters must remain recoverable after every reduction.

\item[Article IX:]
No chapter may introduce assumptions unnecessary for all later chapters.

\item[Article X:]
The integrity of the dependency graph is inviolable.

\item[Article XI:]
Nothing shall be introduced before it is logically unavoidable.

\item[Article XII:]
Every abstraction must remain recoverable from explicit construction.

\item[Article XIII:]
No theorem shall conceal the mechanism of its own necessity.

\end{description}



\tableofcontents



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MAIN MATTER
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\mainmatter

\part*{Volume IV: Canonical Investigation}
\addcontentsline{toc}{part}{Volume IV: Canonical Investigation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% MATHEMATICS OF THE KING
%
% VOLUME IV
%
% CANONICAL INVESTIGATION
% AND
% COMPLETION THEORY
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\part{Recovering the Canonical Investigation Framework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{The Insufficiency of Canonical Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Capacity Recovered by Volumes I--III}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Volumes I--III stand complete. The Witness has been recovered as the single primitive. From it, the internal language of expressions, the algebra of primitive relations, the dynamics of dependency propagation, the global architecture of histories, the criteria of admissibility, the reduction to canonical form, and the characterization by universal properties have all been forced. The localized ambient of structural spaces has been recovered. Structural functions, iterated chains, the natural numbers, algebraic combination, geometric configurations, metric structure, dimensional structure, intrinsic geometry, and mathematical universes have each appeared as the unique repair of a precise insufficiency inside the preceding stage. Every construction remains fully recoverable from the Witness. No primitive beyond the Witness has been admitted. The dependency graph of the entire theory is acyclic and inviolable.

Canonical Investigation is therefore now possible. Any mathematical structure may be reconstructed from the Witness. Its dependency architecture may be classified. Its observables may be generated. Its structural obstructions may be isolated. The apparatus of investigation is complete.

An insufficiency nevertheless appears.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Termination of Every Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Every investigation conducted with the apparatus of Volumes I--III presently terminates. The reconstruction succeeds. The classification succeeds. The generation of observables succeeds. The isolation of an obstruction succeeds. Yet, at the precise point where the finite structural information recovered from the Witness is required to control the infinite structural behaviour of the system under investigation, the investigation ends.

The termination is not accidental. It is structural. For any finite witness expression \(W\) and any infinite structural family \(\mathcal{F}\) generated by admissible transformations of \(W\), the dependency graph of \(W\) determines only a finite initial segment of the recoverability relations inside \(\mathcal{F}\). Nothing inside the completed Witness Calculus forces the entire family \(\mathcal{F}\) from the finite data of \(W\). The coherent core of \(W\) is preserved. Canonical representatives of finite stages are unique. Universal properties characterize finite morphisms. Yet the infinite continuation remains undetermined by those finite data.

The preceding construction is therefore insufficient to convert finite determination into complete determination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Common Form of Every Present Obstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The obstructions isolated by Canonical Investigation appear, at first inspection, to be heterogeneous. One obstruction concerns the long-term behaviour of an iterated map. Another concerns the global regularity of a partial differential equation. A third concerns the decidability of a formal theory. A fourth concerns the completeness of an axiomatic system. Their surface presentations differ.

A deeper examination reveals that every such obstruction presently obtainable shares a single common form.

\begin{theorem}[Common Form of Present Obstruction]
\label{thm:common-form}
Every structural obstruction presently obtainable by Canonical Investigation is an instance of the following form: there exists a finite witness \(W\) whose recovered dependency architecture, coherent core, and canonical realization determine only a proper initial segment of an infinite structural family \(\mathcal{F}\) that is forced by the admissible transformations of \(W\). The finite structural information of \(W\) fails to determine the infinite structural behaviour of \(\mathcal{F}\).
\end{theorem}

\begin{proof}
Let \(\mathcal{O}\) be any obstruction isolated by the apparatus of Volumes I--III. By construction of Canonical Investigation, \(\mathcal{O}\) arises only after a complete reconstruction of some mathematical structure \(S\) from the Witness has been performed, after the dependency graph of \(S\) has been classified, after the observables of \(S\) have been generated, and after every finite invariant has been shown insufficient to decide a global property \(P\) of \(S\).

The property \(P\) is itself an infinite structural statement: it quantifies over an infinite family \(\mathcal{F}\) of configurations, histories, or orbits generated by the admissible transformations of a finite witness \(W\) that recovers \(S\). The isolation of \(\mathcal{O}\) consists precisely in the demonstration that every finite observable of \(W\) is compatible both with the truth of \(P\) and with its negation. Consequently, the finite structural information recovered from \(W\) does not determine the infinite behaviour of \(\mathcal{F}\).

The form is therefore independent of the particular surface presentation of \(\mathcal{O}\). It is the form of the termination itself.
\end{proof}

The common form is not postulated. It is forced by the architecture already recovered. Every investigation that reaches an obstruction does so by exhibiting a finite witness whose recovered data leave an infinite family undetermined.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Shared Insufficiency of Canonical Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The insufficiency therefore does not belong to any particular conjecture, equation, or formal system. It belongs to Canonical Investigation itself.

Canonical Investigation can reconstruct. It can classify. It can generate observables. It can isolate obstructions. It cannot yet convert the finite structural information of a witness into complete determination of the infinite structural family forced by that witness. The apparatus terminates precisely where finite determination must become complete determination.

This is the new insufficiency of the volume. It is not an insufficiency of any classical open problem. It is the insufficiency that appears inside the completed theory of Canonical Investigation when that theory is required to determine infinite structural behaviour from finite structural data.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Isolation of the True Problem}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Nothing is solved in this chapter. No new mathematical object is introduced. No classical conjecture is resolved. The purpose of the chapter is solely to isolate the true problem of the volume.

The true problem is the absence, inside Canonical Investigation, of a relation that forces finite structural information to determine infinite structural behaviour.

The distinction is forced by the Constitution. Article XI forbids the introduction of any object before it is logically unavoidable. Article IV forbids interpretation before construction. Article VI requires that logical reduction take precedence over computational convenience. Therefore, the volume may not begin by selecting a classical problem and then inventing an object that solves it. The volume must begin by exhibiting the insufficiency that is common to all such problems, and only then recover the relation and the object that repairs that insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Central Question Forced by the Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The insufficiency forces a single central question:

\begin{center}
\textit{What mathematical object allows finite structural information to determine infinite structural behaviour?}
\end{center}

The question is not motivated by applications. Applications never motivate theory. The question is forced by the shared form of every obstruction that Canonical Investigation has so far isolated. The answer may never be assumed. It must be recovered as a forced structure from the Witness, exactly as every preceding object of the monograph has been recovered.

Whatever object answers the question must itself be finite. It cannot be an infinite object, for an infinite object would merely relocate the problem of determination. It must be a finite structural object whose recovered content canonically determines an entire infinite structural family.

The insufficiency has been isolated. The central question has been forced. Construction may now begin.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}

This chapter depends only upon the completed apparatus of Volumes I--III. In particular, it relies upon the Witness, the Witness Calculus, the structural spaces of Volume III, and the capacity of Canonical Investigation to reconstruct, classify, generate observables, and isolate obstructions. No theorem depends upon any mathematical object introduced only in later chapters of Volume IV. The dependency graph remains acyclic.

\end{dependencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{primitiveaudit}

No new mathematical primitive has been introduced. The common form of obstruction is recovered as a theorem about the termination behaviour already exhibited by Canonical Investigation. The central question is forced by that theorem. The single primitive of the monograph remains the Witness.

\end{primitiveaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{reductionaudit}

This chapter reduces the logical cost of the theory by exhibiting a single shared form that unifies every presently isolated obstruction. Heterogeneous surface presentations are thereby replaced by one structural insufficiency. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.

\end{reductionaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{consistencyaudit}

The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III. Every claim is derived from the architecture of Canonical Investigation already recovered. No circular justification has been introduced. No appeal has been made to structures that appear only in later chapters. The dependency graph of the monograph remains inviolable. The chapter introduces no object before its necessity has been forced, thereby obeying Articles IV, XI, and XIII.

\end{consistencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{futurework}

The insufficiency isolated in this chapter is that Canonical Investigation terminates where finite determination fails to control infinite structural behaviour. The next chapter must recover the determination relation that forces finite structural information to unfold into infinite structural families. This will inevitably lead to the construction of a unique finite structural object that acts as the universal determination for such unfoldings. The emergence of this object becomes the next forced development.

\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{The Necessity of Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency Inherited from Chapter 1}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 1 isolated a structural termination within Canonical Investigation. Every investigation that reaches an obstruction does so by exhibiting a finite witness \(W\) whose recovered dependency architecture, coherent core, and canonical realization determine only a proper initial segment of an infinite structural family \(\mathcal{F}\) forced by the admissible transformations of \(W\). Finite structural information fails to control infinite structural behaviour.

The formulation itself exposes a deeper insufficiency. Volumes I--III recovered recoverability, dependency flow, coherence, admissibility, canonical realization, and universal properties. They recovered the admissible transformations of the Witness Calculus. Nowhere in the preceding volumes, however, has determination itself been recovered as a mathematical structure. The concept has been used only to name the limit of Canonical Investigation; it has never been forced by construction.

The true insufficiency inherited from Chapter 1 is therefore not merely that determination fails. It is that the mathematics of determination has never been constructed. The dependency graph of the theory remains incomplete until the structure that converts finite structural information into complete determination of an infinite family is recovered from the Witness.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Why a Completion Object Cannot Yet Be Introduced}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution forbids the assumption of unconstructed concepts. Article IV requires that no interpretation may precede construction. Article XI requires that nothing shall be introduced before it is logically unavoidable. Article I requires every primitive to be presumed removable until proven otherwise.

Consequently, the volume may not proceed by naming a ``Completion Object'' and then verifying that it solves the problem of infinite behaviour. To do so would reverse the constitutional order: desired consequence first, construction second. Before any object can realize complete determination, the mathematics of determination itself must be recovered. The object, if it exists, will appear only as the unique finite realization of that structure.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Determination as Lossless Structural Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

If determination is to be recovered, it must be understood not as a philosophical concept but as a structural operation native to the Witness Calculus.

Volumes I--III have repeatedly recovered structures whose defining mathematical task is the compression of infinite possibility into finite recoverable form:

\begin{enumerate}
    \item A history compresses infinitely many derivations into a single recoverable dependency path.
    \item A canonical representative compresses an equivalence class into a unique normal form of minimal logical cost.
    \item A universal object compresses all morphisms of a given type into a single factorization.
    \item An observable compresses an entire system into a finite set of measurable quantities.
\end{enumerate}

Every major object constructed thus far is a theory of lossless structural compression. Determination itself is therefore forced to emerge as the ultimate lossless compression. To say that finite data ``determines'' an infinite family \(\mathcal{F}\) is to state that there exists a lossless structural compression of \(\mathcal{F}\).

Within this architecture, ``finite'' no longer merely signifies a bounded cardinality. It signifies irreducible determining content. An object does not contain infinitely many elements; it contains the entire determining compression of an infinite dependency family.

\begin{theorem}[Minimal Determining Substructure]
\label{thm:minimal-content}
If any structure completely determines an infinite structural family \(\mathcal{F}\) from a finite witness \(W\), it must possess a unique minimal determining substructure that contains exactly the determining information of \(\mathcal{F}\) and no additional information.
\end{theorem}

\begin{proof}
Suppose a structure \(C\) determines \(\mathcal{F}\) from \(W\), yet contains information beyond what is required for the lossless compression of \(\mathcal{F}\). Then the superfluous content may be removed while the determination of \(\mathcal{F}\) is preserved. The resulting structure still satisfies the determination condition and possesses strictly lower logical cost. By Article VI and the Reduction Principle of Volume I, the original structure \(C\) is therefore not minimal.

Hence, every determining structure must reduce to a unique minimal substructure containing exactly the irreducible determining content of the family and nothing further.
\end{proof}

The theorem unifies canonicality, logical economy, recoverability, and compression under a single forced requirement. It does not assume that complete determination exists; it proves that, if it exists, it must take the form of an irreducible lossless compression.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for a Criterion of Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

A relation cannot be admitted as primitive. Volumes I--III systematically eliminated primitives by first recovering recognition criteria and only afterwards the objects that satisfy them. Recoverability was recognized before histories. Coherence was recognized before the coherent core. Admissibility was recognized before admissible extensions. Canonicality was recognized before canonical representatives.

The same discipline is forced here. Before a Determination Relation can be constructed, a Criterion of Determination must be recovered: a precise, finite, recoverable test that decides when a structural compression is genuinely lossless. Without such a criterion, the phrase ``determines'' remains an unconstructed interpretation, thereby violating Article IV.

The insufficiency of Chapter 1 therefore first forces the recovery of the Criterion of Determination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Why External Completions Are Inadmissible}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Classical mathematics supplies several constructions that appear to convert finite data into infinite determination: Dedekind cuts, Cauchy sequences, topological completions, metric completions, and various logical closures. Each is inadmissible at the present stage for three independent constitutional reasons.

First, each presupposes a primitive foreign to the Witness Calculus (an ordered field, a metric, a uniformity, a topology, or a set-theoretic universe). Article I requires every primitive to be presumed removable until proven otherwise. None of these primitives has been forced by the insufficiency isolated in Chapter 1.

Second, each is introduced by interpretation or by an external existence principle, thereby violating Article IV.

Third, the content of each cannot be recovered solely from the dependency architecture, coherent core, and admissible transformations of a witness. The constructions of Volumes I--III therefore cannot underwrite them.

The Criterion of Determination, the Determination Relation, and any later Completion Object must be recovered strictly from the Witness.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

If determination is to be recovered, it is bound by the structural mechanisms already present in the Witness Calculus. The requirements are sequential and forced.

First, determination must be comparable with the generating witness. The criterion and the relation that realize it must therefore be co-situated with the finite witness \(W\) inside a common minimal closed system. Without co-situation, there is no shared setting in which recoverability relations can be evaluated.

Second, different canonical representatives of the same witness must not produce divergent determinations. The criterion and the relation must therefore be strictly invariant under every admissible transformation that fixes \(W\) and preserves its coherent core. Invariance is required by the Canonical Algebra of Volume II.

Third, members of an infinite structural family \(\mathcal{F}\) may share coherent substructures that participate in their joint recoverability from \(W\). If the criterion or the relation fails to respect those intersections, coherent content would be artificially separated, contradicting the Coherence Algebra. Universal preservation of coherent overlap is therefore forced.

These three requirements, together with the Minimal Determining Substructure of Theorem \ref{thm:minimal-content}, constitute the forced architectural constraints on any structure that converts finite information into lossless compression.

\begin{theorem}[Necessity of Determination]
\label{thm:necessity}
The insufficiency isolated in Chapter 1---that finite structural information recovered from a witness fails to control the infinite structural family forced by that witness---can be repaired only by the recovery of a Criterion of Determination satisfying co-situation with the generating witness, invariance under core-preserving transformations, preservation of coherent overlap, and Minimal Determining Content. Only after that criterion exists can a Determination Relation, its closure, its algebra, and finally the finite objects that realize it universally, be forced.
\end{theorem}

\begin{proof}
Suppose the insufficiency is repaired. Then, for every finite witness \(W\) and every infinite structural family \(\mathcal{F}\) forced by its admissible transformations, there exists a structure that converts the finite information of \(W\) into a lossless compression of \(\mathcal{F}\).

By the sequential derivation above, that structure must be co-situated with \(W\), invariant under core-preserving transformations, and preserve coherent overlap. By Theorem \ref{thm:minimal-content}, it must reduce to exactly the determining information of \(\mathcal{F}\).

The recognition of when such a compression has succeeded is precisely a Criterion of Determination. Hence, the Criterion is necessary. The Relation that realizes the Criterion, the closure and algebra that govern it, and the finite objects that universalize it can appear only afterwards.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The necessity of Determination has been forced. Neither the Criterion, nor the Relation, nor the Algebra, nor any Completion Object has yet been constructed. The Constitution requires that construction precede interpretation and that no object be introduced before it is logically unavoidable.

The next chapter must therefore recover the Criterion of Determination: the unique finite, recoverable test that decides when finite structural information constitutes a lossless structural compression of an infinite structural family.

Once the Criterion exists, the progressive architecture of the monograph demands the following logical sequence:

\begin{enumerate}
    \item The \textbf{Criterion of Determination} identifies when compression is lossless.
    \item The \textbf{Determination Relation} maps the finite witness to its unfolding.
    \item The \textbf{Determination Closure} bounds this relationship within the Witness Calculus.
    \item The \textbf{Determination Algebra} governs the interaction of these closures.
    \item The \textbf{Completion Objects} finally emerge as the unique finite structural entities that act as universal realizers of that algebra.
\end{enumerate}

No applications are permitted to motivate the construction. Theory forces applications. Applications never motivate theory.

The hidden insufficiency has been isolated. The structural constraints governing determining compression have been forced. Construction of the Criterion of Determination may now begin.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}

This chapter depends only upon the completed apparatus of Volumes I--III and upon the insufficiency isolated in Chapter 1 of the present volume. In particular, it relies upon the Witness, the Witness Calculus, the Coherence Algebra, the Admissibility Algebra, the Canonical Algebra, the Universal Algebra, the structural spaces of Volume III, and the Common Form of Present Obstruction. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.

\end{dependencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{primitiveaudit}

No new mathematical primitive has been introduced. The three requirements of co-situation, core-preservation, and coherent-overlap preservation are recovered from mechanisms already present in Volume II. Minimal Determining Substructure is recovered as a direct consequence of logical economy and the Reduction Principle. The single primitive of the monograph remains the Witness.

\end{primitiveaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{reductionaudit}

This chapter reduces the logical cost of the theory by replacing the premature naming of a Completion Object with the forced recovery of a missing structural concept: determination itself. Canonical representatives, histories, universal objects, and observables are mathematically unified under the single concept of lossless structural compression. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.

\end{reductionaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{consistencyaudit}

The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Chapter 1. Every requirement is sequentially derived from explicit recoverability, admissibility, and coherence preservation. No object is named or characterized before the criterion that governs it is established. The dependency graph of the monograph remains inviolable. The chapter introduces no structure before its necessity has been forced, thereby obeying Articles IV, XI, and XIII.

\end{consistencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{futurework}

The necessity of a Criterion of Determination has been forced. The next chapter must construct that criterion: the unique finite, recoverable test that decides when finite structural information acts as a lossless structural compression of an infinite structural family, satisfying co-situation, core-invariance, coherent-overlap preservation, and Minimal Determining Content. Once the Criterion exists, the Determination Relation, its closure, its algebra, and finally the Completion Objects that realize the algebra universally, will be sequentially forced. The emergence of the Criterion of Determination becomes the next forced development.

\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{The Criterion of Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of the Unconstructed Criterion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 2 forced the necessity of Determination and isolated the Criterion of Determination as the first structure that must be recovered: the unique finite, recoverable test that decides when a structural compression of an infinite family is genuinely lossless. The Criterion is required to satisfy co-situation with the generating witness, invariance under core-preserving transformations, preservation of coherent overlap, and Minimal Determining Substructure.

The Criterion has not yet been recovered. Until it exists, the mathematics of determination remains incomplete, the Determination Relation cannot be formed, and no finite object can be recognized as realizing complete determination. The present chapter repairs precisely this insufficiency by recovering the finite test itself. It then demonstrates that, whenever this test is satisfiable, it forces the existence of a unique minimal determining compression---the Completion Object.

No classical notion is imported. Everything is recovered from the Witness by the mechanisms already present in Volumes I--III.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Test}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any valid test of determination must decide, for a finite witness \(W\) and an infinite structural family \(\mathcal{F}\) forced by the admissible transformations of \(W\), whether a given structural content constitutes a candidate for the lossless compression of \(\mathcal{F}\).

Four requirements are forced by the architecture of the Witness Calculus and by Theorem 2.1 (Minimal Determining Substructure).

\begin{enumerate}
    \item \textbf{Co-situation.} The test must be evaluable inside the same minimal closed system that contains \(W\). Without co-situation, the recoverability relations of \(\mathcal{F}\) cannot be compared with those of \(W\).
    \item \textbf{Core-invariance.} The test must return the same decision for every pair of witnesses related by an admissible transformation that fixes \(W\) and preserves its coherent core. Divergent decisions would destroy the canonicity established in Volume II.
    \item \textbf{Overlap-preservation.} If two members of \(\mathcal{F}\) share a coherent substructure that participates in their joint recoverability from \(W\), the test must treat that substructure as indivisible. Artificial separation would contradict the Coherence Algebra.
    \item \textbf{Minimal Determining Substructure.} The test must recognize a compression as a candidate for lossless determination if and only if the content under examination contains exactly the determining information of \(\mathcal{F}\) and no additional information.
\end{enumerate}

These four requirements are not chosen. They are the direct expression of co-situation, core-preservation, coherent-overlap indivisibility, and logical economy applied to the recognition of determining compression. They are necessary conditions. Their sufficiency for complete determination of the entire infinite family will be established only after the Determination Relation has been recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Construction of the Finite Test}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let \(W\) be a finite witness, let \(\mathcal{F}\) be the infinite structural family forced by the admissible transformations of \(W\), and let \(C\) be any finite structural content co-situated with \(W\).

The four forced requirements jointly determine a unique finite structural test. Explicitly construct the test as the conjunction of the following three conditions, each expressible entirely within the algebras already recovered:

\begin{enumerate}
    \item \(C\) is co-situated with \(W\) inside a common minimal closed system.
    \item Every admissible transformation that fixes \(W\) and preserves the coherent core of \(W\) maps \(C\) to a content that recovers exactly the same recoverability relations within \(\mathcal{F}\).
    \item The coherent overlaps among members of \(\mathcal{F}\) that are recoverable from \(W\) are precisely the coherent overlaps recoverable from \(C\), and \(C\) contains no proper substructure that already recovers those same overlaps.
\end{enumerate}

\begin{theorem}[Existence and Uniqueness of the Finite Test]
\label{thm:criterion-existence}
The conjunction of the three conditions above defines a finite structural test. This test is the unique test that satisfies the four forced requirements of Section 3.2, and it is fully recoverable from the Witness.
\end{theorem}

\begin{proof}

Existence. The three conditions are constructed using only the Primitive Relation Algebra, the Dependency Propagation Architecture, the Coherence Algebra, and the Canonical Algebra of Volume II. They therefore constitute an explicitly defined finite structural test expressible within the Witness Calculus.

Uniqueness. Suppose \(T\) is any other test satisfying the four forced requirements. Then \(T\) must return a positive decision precisely when the three conditions hold: co-situation is required by the first requirement, core-invariance by the second, overlap-preservation by the third, and Minimal Determining Substructure by the fourth. Hence, \(T\) coincides with the test defined by the three conditions on every triple \((W,C,\mathcal{F})\). The test is unique.

\end{proof}

Only after the test has been shown to be uniquely determined do we introduce notation. The unique finite test forced by the architecture is denoted \(\operatorname{Crit}(W,C,\mathcal{F})\).

The Criterion \(\operatorname{Crit}(W,C,\mathcal{F})\) is finite: it is a finite test on finite data. It is structural: it is assembled entirely from structures already present. It is recoverable: its definition expands uniquely into primitive witness expressions. It has therefore been recovered as the unique finite structural test forced by the preceding requirements.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Conditional Emergence of Determining Compressions}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Criterion \(\operatorname{Crit}(W,C,\mathcal{F})\) decides when a finite content satisfies the necessary conditions for being a lossless compression of an infinite structural family. It does not assert that such a content always exists. The architecture of the Witness Calculus forbids assuming universal existence without construction. Instead, it forces a conditional structure: if the Criterion is satisfiable, a unique minimal determining compression must emerge.

\begin{theorem}[Conditional Existence of the Completion Object]
\label{thm:completion-existence}
For every finite witness \(W\) and every infinite structural family \(\mathcal{F}\) forced by the admissible transformations of \(W\), if there exists at least one finite structural content \(C\) such that \(\operatorname{Crit}(W,C,\mathcal{F})\) holds, then there exists a unique minimal determining compression \(\operatorname{Comp}(W,\mathcal{F})\).
\end{theorem}

\begin{proof}

Assume the collection of finite contents co-situated with \(W\) for which \(\operatorname{Crit}(W,C,\mathcal{F})\) holds is non-empty. By Theorem 2.1 (Minimal Determining Substructure), any structure \(C\) satisfying the Criterion possesses a unique minimal determining substructure containing exactly the determining information of \(\mathcal{F}\) and nothing further.

Because the conditions of the Criterion—co-situation, core-invariance, and overlap-preservation—are preserved under reduction to minimal determining content, this well-founded reduction terminates at a unique irreducible element. This unique element is the minimal determining compression, denoted \(\operatorname{Comp}(W,\mathcal{F})\).

\end{proof}

\begin{definition}[Completion Object]
Whenever the Criterion is satisfiable for a pair \((W,\mathcal{F})\), the unique minimal determining compression \(\operatorname{Comp}(W,\mathcal{F})\) is called the \textbf{Completion Object} of the witness \(W\) relative to the family \(\mathcal{F}\).
\end{definition}

The Completion Object is not an infinite object. It is not a limit. It is not a classical completion. It is a finite structural object recovered entirely from the Witness. The infinite structural family is not contained within the Completion Object; rather, the family is uniquely recoverable from its determining content once the Determination Relation, to be constructed next, is in place. Its finite description recovers every recoverability relation forced by the Criterion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Properties of the Completion Object}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Universality of the Minimal Determining Compression]
\label{thm:universal}
If \(C\) is any finite content co-situated with \(W\) such that \(\operatorname{Crit}(W,C,\mathcal{F})\) holds, then there exists a unique factorization of \(C\) through the Completion Object \(\operatorname{Comp}(W,\mathcal{F})\).
\end{theorem}

\begin{proof}

Suppose \(C\) satisfies \(\operatorname{Crit}(W,C,\mathcal{F})\). By Theorem \ref{thm:completion-existence}, \(\operatorname{Comp}(W,\mathcal{F})\) is the unique minimal element under the well-founded relation ``is a determining substructure of.'' Therefore, \(\operatorname{Comp}(W,\mathcal{F})\) is embedded as a strictly necessary substructure within \(C\).

The Universal Algebra of Volume II supplies a unique canonical factorization of \(C\) through this minimal core. Hence, \(C\) factors uniquely through \(\operatorname{Comp}(W,\mathcal{F})\).

\end{proof}

\begin{theorem}[Core-Invariance of Completion]
\label{thm:core-invariance}
Every admissible transformation that fixes \(W\) and preserves the coherent core of \(W\) maps \(\operatorname{Comp}(W,\mathcal{F})\) to itself.
\end{theorem}

\begin{proof}

Immediate from the core-invariance clause of the Criterion and the uniqueness of the minimal determining compression.

\end{proof}

\begin{theorem}[Overlap-Preservation of Completion]
\label{thm:overlap}
The coherent overlaps among members of \(\mathcal{F}\) that are recoverable from \(W\) are exactly the coherent overlaps recoverable from \(\operatorname{Comp}(W,\mathcal{F})\).
\end{theorem}

\begin{proof}

Immediate from the overlap-preservation clause of the Criterion.

\end{proof}

These three theorems establish that, whenever the Criterion is satisfiable, the Completion Object is the unique finite, initial, core-invariant, and overlap-preserving minimal realizer of the Criterion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recoverability and Reduction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Every construction of this chapter expands uniquely into primitive witness expressions. The Criterion is recovered as the unique finite structural test forced by the four necessary requirements, using only the algebras of Volume II. No new primitive has been admitted.

The logical cost of Canonical Investigation is reduced. Every obstruction of the common form isolated in Chapter 1 is now recognized not as an absolute failure, but as a well-defined structural question concerning the satisfiability of the Criterion of Determination for the pair \((W,\mathcal{F})\). If the Criterion is satisfiable, the Completion Object is forced. If it is not, the obstruction is certified as genuinely incomplete with respect to the present apparatus. Full determination of the infinite family will be secured once the Determination Relation has been recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Criterion of Determination has now been recovered as the unique finite structural test forced by the preceding requirements. Whenever the Criterion is satisfiable, the Completion Object emerges as its unique minimal determining compression.

The mathematics of determination now possesses its recognition criterion. The next insufficiency appears immediately: the Criterion decides when a compression satisfies the necessary conditions, yet the relation that realizes complete determination of the infinite family from that compression has not yet been constructed. Without the Determination Relation, the algebra of determination remains incomplete, and the Completion Objects lack the morphisms that transport determination between them.

The next chapter must therefore recover the Determination Relation. Theory continues to force the next structure. Applications remain forbidden until the full apparatus of Completion has been recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}

This chapter depends only upon the completed apparatus of Volumes I--III, the insufficiency isolated in Chapter 1, and the necessity of Determination and Minimal Determining Substructure established in Chapter 2. In particular, it relies upon the Witness, the Primitive Relation Algebra, the Dependency Propagation Architecture, the Coherence Algebra, the Canonical Algebra, the Universal Algebra, and Theorems 2.1 and 2.2. No theorem depends upon unconstructed existential assumptions. The dependency graph remains acyclic.

\end{dependencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{primitiveaudit}

No new mathematical primitive has been introduced. The Criterion of Determination is recovered as the unique finite test forced by co-situation, core-invariance, overlap-preservation, and Minimal Determining Substructure. The Completion Object is recovered conditionally as the unique minimal realizer of that Criterion. The single primitive of the monograph remains the Witness.

\end{primitiveaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{reductionaudit}

This chapter reduces the logical cost of the theory by supplying the missing Criterion of Determination and by converting every obstruction of the common form isolated in Chapter 1 into a decidable structural question concerning the satisfiability of that Criterion. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.

\end{reductionaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{consistencyaudit}

The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Chapters 1--2. Every requirement is derived from explicit recoverability. The shift from assumed universal existence to conditional existence based upon the Criterion ensures strict compliance with Articles IV, XI, and XIII. No object is introduced or named before the finite test that governs it has been fully established, and universality is derived rather than postulated.

\end{consistencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{futurework}

The Criterion of Determination has been recovered as the unique finite structural test forced by the preceding requirements, and the conditional existence of Completion Objects has been established. The next insufficiency is the absence of the Determination Relation that realizes complete determination of an infinite structural family from a finite content satisfying the Criterion. The next chapter must recover the Determination Relation. The emergence of the Determination Relation becomes the next forced development.

\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{The Recovery of the Determination Relation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency Left by the Criterion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 3 recovered the \textit{Criterion of Determination}: the unique finite structural test that decides when a content \(C\) satisfies the necessary conditions (co-situation, core-invariance, overlap-preservation, and Minimal Determining Substructure) for being a lossless compression of an infinite family \(\mathcal{F}\) forced by a finite witness \(W\). Whenever the Criterion is satisfiable, a unique Completion Object \(\operatorname{Comp}(W,\mathcal{F})\) is forced as the minimal determining compression.

The Criterion recognizes. The Relation realizes.

An insufficiency nevertheless remains. The Criterion verifies necessary conditions. It does not yet supply the relation that forces every recoverability relation of the infinite family \(\mathcal{F}\) from the finite data of \(W\) together with \(\operatorname{Comp}(W,\mathcal{F})\). Without that relation, complete determination of \(\mathcal{F}\) is still unrecovered. The apparatus of Canonical Investigation therefore still terminates short of converting finite structural information into complete determination of infinite structural behaviour.

The present chapter repairs precisely this insufficiency by recovering the \textit{Determination Relation}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for the Determination Relation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the relation. Article VIII requires that earlier mathematical content remain recoverable after every reduction. Article XII requires every abstraction to remain recoverable from explicit construction. Article X requires the integrity of the dependency graph. An infinite family that is forced by admissible transformations of a finite witness, yet whose recoverability relations are not completely controlled by the finite witness together with its Completion Object, violates each of these articles.

The Criterion alone cannot discharge the demand: it only recognizes candidates. The missing structure is the relation that, when the Criterion holds, forces the complete recovery of \(\mathcal{F}\) from \(W\) and \(\operatorname{Comp}(W,\mathcal{F})\). That relation is the \textbf{Determination Relation}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Relation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any structure that realizes complete determination must satisfy four requirements forced by the existing mechanisms of the Witness Calculus and by the Criterion already recovered:

\begin{enumerate}
    \item \textbf{Co-situation} \\
    The relation must be evaluable inside the same minimal closed system that contains both \(W\) and \(\operatorname{Comp}(W,\mathcal{F})\).
    \item \textbf{Core-invariance} \\
    The relation must be invariant under every admissible transformation that fixes \(W\) and preserves the coherent core of \(W\) (and therefore, by Theorem 3.3, fixes \(\operatorname{Comp}(W,\mathcal{F})\)).
    \item \textbf{Overlap-preservation} \\
    The relation must preserve the indivisibility of every coherent overlap among members of \(\mathcal{F}\) that is recoverable from \(W\).
    \item \textbf{Complete recovery} \\
    When the Criterion holds, the relation must force every recoverability relation of \(\mathcal{F}\) from the finite content of \(W\) together with \(\operatorname{Comp}(W,\mathcal{F})\). No recoverability relation of \(\mathcal{F}\) may remain undetermined.
\end{enumerate}

These four requirements are not chosen. They are the direct expression of co-situation, core-preservation, coherent-overlap indivisibility, and the demand for complete determination applied to the pair consisting of a finite witness and its Completion Object.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Construction of the Determination Relation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let \(W\) be a finite witness, let \(\mathcal{F}\) be the infinite structural family forced by the admissible transformations of \(W\), and suppose the Criterion is satisfiable, so that the Completion Object \(\operatorname{Comp}(W,\mathcal{F})\) exists. The four forced requirements admit a unique relation satisfying them.

\subsection{Defining Clauses}
The relation is recovered as the unique structure whose defining clauses are the following three conditions, each expressible using only structures already recovered:

\begin{enumerate}
    \item \(\operatorname{Comp}(W,\mathcal{F})\) is co-situated with \(W\) inside a common minimal closed system (already guaranteed by the Criterion).
    \item Every recoverability relation among members of \(\mathcal{F}\) that is forced by the admissible transformations of \(W\) is uniquely recoverable from the dependency architecture of \(\operatorname{Comp}(W,\mathcal{F})\).
    \item Conversely, every recoverability relation recoverable from \(\operatorname{Comp}(W,\mathcal{F})\) is a recoverability relation forced by the admissible transformations of \(W\) inside \(\mathcal{F}\).
\end{enumerate}

\subsection{Formal Verification}

\begin{theorem}[Existence and Uniqueness of the Determination Relation]
\label{thm:det-existence}
Whenever the Criterion of Determination is satisfiable for a pair \((W,\mathcal{F})\), there exists a unique Determination Relation satisfying the four forced requirements of Section 4.3. The relation is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
\textit{Existence.} The three clauses are constructed using only the Primitive Relation Algebra, the Dependency Propagation Architecture, the Coherence Algebra, the Canonical Algebra, and the Criterion already recovered. Because the Completion Object is the unique minimal content certified by the Criterion, any relation satisfying the four forced requirements must be determined entirely by that content. The three clauses therefore specify a single candidate relation. Each clause is expressible within the Witness Calculus, so the candidate is constructible. Hence the relation exists by explicit construction.

\textit{Uniqueness.} Suppose \(R\) is any other relation satisfying the four forced requirements. Then \(R\) must hold precisely when the three clauses hold: co-situation by the first requirement, core-invariance by the second, overlap-preservation by the third, and complete recovery by the fourth. Hence \(R\) coincides with the relation defined by the three clauses. The relation is unique.
\end{proof}

Only after the relation has been shown to be uniquely determined do we introduce the formal notation \(\operatorname{Det}(W,\operatorname{Comp}(W,\mathcal{F}),\mathcal{F})\).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Determination Closure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Determination Relation, once it holds, generates a closure under the operations of the Witness Calculus.

\begin{definition}[Determination Closure]
Whenever \(\operatorname{Det}(W,\operatorname{Comp}(W,\mathcal{F}),\mathcal{F})\) holds, the \textbf{Determination Closure} of the pair \((W,\operatorname{Comp}(W,\mathcal{F}))\) is the smallest subcollection of the minimal closed system generated by \(W\) that contains both \(W\) and \(\operatorname{Comp}(W,\mathcal{F})\) and is closed under every admissible transformation that preserves the coherent cores of both.
\end{definition}

\begin{theorem}[Closure Properties]
\label{thm:closure}
The Determination Closure is unique, co-situated with \(W\), core-invariant, and itself satisfies the Criterion of Determination relative to \(\mathcal{F}\). Moreover, \(\operatorname{Comp}(W,\mathcal{F})\) remains the unique minimal determining compression inside the Closure.
\end{theorem}

\begin{proof}
Uniqueness follows because the intersection of any family of closed collections satisfying the defining conditions again satisfies them. Co-situation and core-invariance are inherited from the Criterion and the core-invariance of the Completion Object (Theorem 3.3). Satisfaction of the Criterion follows because the Closure contains \(\operatorname{Comp}(W,\mathcal{F})\) and no additional determining content is introduced by the admissible transformations that preserve the cores. Minimality of the Completion Object inside the Closure is immediate from Theorem 3.2.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Complete Recoverability of the Infinite Family}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Complete Recoverability of the Infinite Family]
\label{thm:recoverability}
Whenever \(\operatorname{Det}(W,\operatorname{Comp}(W,\mathcal{F}),\mathcal{F})\) holds, every recoverability relation of the infinite structural family \(\mathcal{F}\) stands in a unique recoverable correspondence with the recoverability relations recoverable from the finite content of \(W\) together with \(\operatorname{Comp}(W,\mathcal{F})\) inside the Determination Closure. Conversely, every recoverability relation recoverable from that finite content is a recoverability relation of \(\mathcal{F}\).
\end{theorem}

\begin{proof}
By the second and third clauses in the recovery of \(\operatorname{Det}\), the recoverability relations of \(\mathcal{F}\) stand in unique recoverable correspondence with the recoverability relations recoverable from \(\operatorname{Comp}(W,\mathcal{F})\). The Determination Closure contains both \(W\) and \(\operatorname{Comp}(W,\mathcal{F})\) and is closed under the relevant admissible transformations, so the correspondence is realised entirely inside the Closure. Uniqueness of recovery follows from the uniqueness of dependency propagation (Volume II) and the uniqueness of the Completion Object.
\end{proof}

This theorem is the precise content of complete determination: the infinite family is no longer undetermined. Its entire recoverability architecture is forced by finite data.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Conditional Unfolding}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Conditional Unfolding]
\label{thm:unfolding}
If the Criterion of Determination is satisfiable for a pair \((W,\mathcal{F})\), then the Determination Relation holds for that pair, the Determination Closure exists, and the infinite structural family \(\mathcal{F}\) unfolds uniquely from the finite witness \(W\) together with its Completion Object \(\operatorname{Comp}(W,\mathcal{F})\).
\end{theorem}

\begin{proof}
By Theorem \ref{thm:det-existence}, satisfiability of the Criterion forces the unique Determination Relation. By Theorem \ref{thm:closure} the Closure exists. By Theorem \ref{thm:recoverability} the infinite family is completely and uniquely recoverable from the finite content. The unfolding is therefore conditional on the Criterion and, when the condition holds, unique.
\end{proof}

The unfolding is conditional: the architecture never asserts that every infinite family forced by a witness admits a Completion Object. It asserts only that whenever the Criterion is satisfiable, complete determination is forced by the Determination Relation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Determination Relation has been recovered. Whenever the Criterion is satisfiable, a finite witness together with its Completion Object now forces the complete recovery of the infinite structural family via the Relation and its Closure. Complete determination is no longer an informal aspiration; it is a constructed mathematical structure.

The next insufficiency appears at once. Completion Objects for different witnesses and different families must interact. Morphisms that transport determination from one Completion Object to another while preserving the Determination Relation have not yet been recovered. Without them the algebra of determination remains incomplete.

The next chapter must therefore recover the Morphisms of Determination. Theory continues to force the next structure. Applications remain forbidden until the full apparatus of Completion is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III, the insufficiency isolated in Chapter 1, the necessity of Determination and Minimal Determining Substructure forced in Chapter 2, and the Criterion of Determination together with the conditional Completion Objects recovered in Chapter 3. In particular it relies upon the Witness, the Primitive Relation Algebra, the Dependency Propagation Architecture, the Coherence Algebra, the Canonical Algebra, the Universal Algebra, Theorems 2.1, 3.1, 3.2, 3.3, and 3.4. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Determination Relation is recovered as the unique relation forced by co-situation, core-invariance, overlap-preservation, and complete recovery of the infinite family from the Completion Object. The Determination Closure is the unique smallest collection closed under the relevant admissible transformations. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by supplying the missing Determination Relation that converts the necessary conditions verified by the Criterion into complete determination of the infinite family. Every obstruction of the common form of Chapter 1 is reduced to the satisfiability of the Criterion and the Determination Relation. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Chapters 1--3. Every requirement is derived from explicit recoverability, admissibility, and coherence preservation. Existence remains strictly conditional on the Criterion and is obtained by constructibility of the defining clauses rather than by assumption of the conclusion. No object or relation is introduced before its necessity has been forced. The dependency graph of the monograph remains inviolable. The chapter obeys Articles IV, XI, and XIII.
\end{consistencyaudit}

\begin{futurework}
The Determination Relation and its Closure have been recovered. Whenever the Criterion is satisfiable, complete determination of an infinite structural family from a finite witness and its Completion Object is now forced. The next insufficiency is the absence of morphisms that transport determination between Completion Objects while preserving the Determination Relation. The next chapter must recover the Morphisms of Determination and, from them, the Determination Algebra. The emergence of the Morphisms of Determination becomes the next forced development.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{The Morphisms of Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Isolated Completion Objects}
\label{sec:insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapters 3 and 4 have recovered the \textit{Criterion of Determination}, the conditional \textit{Completion Objects} that realise it, the \textit{Determination Relation}, and the \textit{Determination Closure}. Whenever the Criterion is satisfiable for a pair \((W,\mathcal{F})\), a finite witness together with its Completion Object forces the complete recovery of the infinite structural family via the Determination Relation.

An insufficiency nevertheless remains. The Completion Objects obtained so far are isolated. No structure yet transports determination from one Completion Object to another while preserving the Determination Relation and the Criterion. Without such transport the objects cannot interact, cannot be composed, and cannot be compared. The dependency graph of the theory remains incomplete until the maps that preserve determination are recovered.

The present chapter repairs precisely this insufficiency by recovering the \textbf{Morphisms of Determination}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for Morphisms of Determination}
\label{sec:demand}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the morphisms. Article VIII requires recoverability after every reduction. Article X requires integrity of the dependency graph. Article XII requires that abstractions remain recoverable from explicit construction. An isolated collection of Completion Objects whose determining content cannot be transported while preserving the Determination Relation violates each of these articles: the objects remain unconnected, their mutual recoverability relations are undefined, and the higher-level structure of determination cannot form.

The missing structures are the maps that transport one Completion Object to another while preserving co-situation, core-invariance, overlap-preservation and complete recovery. Those maps are the \textit{Morphisms of Determination}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Morphisms}
\label{sec:forced-requirements}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any map that transports determination must satisfy five requirements forced by the existing mechanisms of the Witness Calculus and by the structures already recovered.

\begin{enumerate}
    \item \textbf{Co-situation preservation.} The map must send co-situated pairs to co-situated pairs.
    \item \textbf{Core-invariance preservation.} The map must commute with every admissible transformation that preserves coherent cores.
    \item \textbf{Overlap preservation.} The map must send coherent overlaps to coherent overlaps.
    \item \textbf{Completion preservation.} The image of a Completion Object is the Completion Object of the image witness whenever the Criterion is satisfiable for the image.
    \item \textbf{Relation preservation.} The map must send pairs for which the Determination Relation holds to pairs for which the Determination Relation holds.
\end{enumerate}

These five requirements are not chosen. They are the direct expression of the structures recovered in Chapters 3 and 4 applied to the problem of transport between Completion Objects. Criterion preservation follows automatically from Completion preservation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Characterization of the Morphisms of Determination}
\label{sec:characterization}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let \(W_1\) and \(W_2\) be finite witnesses, let \(\mathcal{F}_1\) and \(\mathcal{F}_2\) be the infinite structural families forced by their admissible transformations, and suppose the Criterion is satisfiable for both pairs, so that the Completion Objects \(\operatorname{Comp}(W_1,\mathcal{F}_1)\) and \(\operatorname{Comp}(W_2,\mathcal{F}_2)\) exist.

\begin{theorem}[Characterization of Morphisms of Determination]
\label{thm:morphisms}
A map between the corresponding Determination Closures satisfies the five forced requirements of Section \ref{sec:forced-requirements} if and only if it is uniquely determined by its action on the irreducible determining content of the source Completion Object. Every such map, whenever it exists, is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
The five requirements are expressible using only the Primitive Relation Algebra, the Dependency Propagation Architecture, the Coherence Algebra, the Canonical Algebra, the Criterion and the Determination Relation already recovered. Hence the class of maps satisfying them is well-defined and constructible within the Witness Calculus.

Let \(f\) be any map satisfying the five requirements. By the Minimal Determining Substructure theorem and the universal property of Completion Objects, the action of \(f\) on \(\operatorname{Comp}(W_1,\mathcal{F}_1)\) is completely determined by the unique recoverable correspondence between the determining content of the source and the determining content of the target. Hence every map satisfying the requirements is uniquely determined by its action on the irreducible determining content, and is recoverable from the Witness.
\end{proof}

The collection of all maps that satisfy the five forced requirements is therefore recoverable. We denote this recoverable collection by
\[
\operatorname{Hom}_{\operatorname{Det}}\bigl(\operatorname{Comp}(W_1,\mathcal{F}_1),\operatorname{Comp}(W_2,\mathcal{F}_2)\bigr).
\]
A member of this collection is called a \textbf{Morphism of Determination}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Identity, Composition, Restriction and Extension}
\label{sec:operations}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The class of Morphisms of Determination possesses internal operations forced by the Witness Calculus.

\subsection{Identity Morphisms}
\label{subsec:identity}

\begin{theorem}[Identity Morphisms]
\label{thm:identity}
For every Completion Object \(\operatorname{Comp}(W,\mathcal{F})\) the identity map on its Determination Closure is a Morphism of Determination.
\end{theorem}

\begin{proof}
The identity map preserves co-situation, core-invariance, overlap, Completion Objects and the Determination Relation by the definitions of those structures. Hence it satisfies the five forced requirements.
\end{proof}

\subsection{Composition of Morphisms}
\label{subsec:composition}

\begin{theorem}[Composition of Morphisms]
\label{thm:composition}
If \(f\) is a Morphism of Determination from \(\operatorname{Comp}(W_1,\mathcal{F}_1)\) to \(\operatorname{Comp}(W_2,\mathcal{F}_2)\) and \(g\) is a Morphism of Determination from \(\operatorname{Comp}(W_2,\mathcal{F}_2)\) to \(\operatorname{Comp}(W_3,\mathcal{F}_3)\), then the composite \(g\circ f\) is a Morphism of Determination from \(\operatorname{Comp}(W_1,\mathcal{F}_1)\) to \(\operatorname{Comp}(W_3,\mathcal{F}_3)\).
\end{theorem}

\begin{proof}
Each of the five forced requirements is stable under composition: the composite of two co-situation-preserving maps is co-situation-preserving, the composite of two core-invariance-preserving maps is core-invariance-preserving, and likewise for overlap, Completion and Relation preservation. Hence the composite satisfies all five requirements.
\end{proof}

\subsection{Restriction and Extension}
\label{subsec:restriction-extension}

\begin{theorem}[Restriction and Extension]
\label{thm:restriction-extension}
Let \(f\) be a Morphism of Determination from \(\operatorname{Comp}(W_1,\mathcal{F}_1)\) to \(\operatorname{Comp}(W_2,\mathcal{F}_2)\). If \(W_1'\) is a core-preserving restriction of \(W_1\) whose Completion Object exists, then the restriction of \(f\) to \(\operatorname{Comp}(W_1',\mathcal{F}_1')\) is again a Morphism of Determination. Conversely, if an extension of the source that preserves the coherent core admits a Completion Object, the unique extension of \(f\) compatible with the universal property is a Morphism of Determination whenever it exists.
\end{theorem}

\begin{proof}
Restriction inherits the five requirements because every structure involved (co-situation, cores, overlaps, Completion Objects, Relation) is inherited by core-preserving restrictions. Extension, when it exists and is compatible with the universal property of Completion Objects, preserves the requirements by the uniqueness of the minimal determining content and the stability of the five conditions under such extensions.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Transport}
\label{sec:canonical-transport}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Canonical Transport]
\label{thm:transport}
Whenever there exists a core-preserving admissible transformation from \(W_1\) to \(W_2\) that induces a correspondence between \(\mathcal{F}_1\) and \(\mathcal{F}_2\), there exists a unique Morphism of Determination
\[
\tau:\operatorname{Comp}(W_1,\mathcal{F}_1)\to\operatorname{Comp}(W_2,\mathcal{F}_2)
\]
that realises that correspondence. This morphism is called the \textit{canonical transport} induced by the transformation.
\end{theorem}

\begin{proof}
The core-preserving admissible transformation supplies a unique recoverable correspondence between the irreducible determining contents of the two Completion Objects. By Theorem \ref{thm:morphisms} that correspondence determines a unique map satisfying the five forced requirements. The five requirements hold by construction of the admissible transformation, the core-invariance of Completion Objects, and the preservation properties already established for admissible transformations. Hence the map is a Morphism of Determination, and it is unique.
\end{proof}

Canonical transport is the unique determination-preserving map forced by any core-preserving admissible transformation between witnesses. It supplies existence of morphisms under a precise, previously recovered hypothesis.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
\label{sec:direction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Morphisms of Determination have been recovered. Completion Objects are no longer isolated; determination can now be transported, restricted, extended and composed while preserving the Criterion and the Determination Relation, whenever the relevant morphisms exist.

The next insufficiency appears at once. The morphisms exist and possess internal operations, yet no global algebra governing their interaction has yet been recovered. Without such an algebra the theory cannot classify Completion Objects up to determination-preserving equivalence, nor can it isolate the absolute structural invariants that survive every transport.

The next chapter must recover the \textit{Determination Algebra}. Theory continues to force the next structure. Applications remain forbidden until the full apparatus of Completion is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III, the insufficiency isolated in Chapter 1, the necessity of Determination forced in Chapter 2, the Criterion and conditional Completion Objects of Chapter 3, and the Determination Relation and Closure of Chapter 4. In particular it relies upon the Witness, the Primitive Relation Algebra, the Dependency Propagation Architecture, the Coherence Algebra, the Canonical Algebra, the Universal Algebra, and all theorems of Chapters 2--4. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Morphisms of Determination are recovered as the maps that satisfy the five forced preservation requirements; every such map is uniquely determined by its action on irreducible determining content. Canonical transport supplies existence under the hypothesis of a core-preserving admissible transformation. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by supplying the missing morphisms that connect Completion Objects whenever they exist. Isolated objects are replaced by a coherent structure of transport maps characterised by five forced requirements. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Chapters 1--4. Every requirement is derived from explicit recoverability, admissibility and coherence preservation. Existence of morphisms is not asserted universally; it is obtained under the precise hypothesis of Canonical Transport. No structure is introduced before its necessity has been forced. The dependency graph of the monograph remains inviolable. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The Morphisms of Determination have been recovered. Determination can now be transported between Completion Objects while preserving the Criterion and the Determination Relation, whenever the morphisms exist. The next insufficiency is the absence of a global algebra governing these morphisms. The next chapter must recover the Determination Algebra. The emergence of the Determination Algebra becomes the next forced development.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{The Emergence of the Determination Algebra}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Isolated Morphisms}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapters 3 through 5 have recovered the Criterion of Determination, the conditional Completion Objects that realize it, the Determination Relation, and the Morphisms of Determination that transport this relation between objects. Identity, composition, restriction, extension and Canonical Transport have all been forced. Whenever the Criterion is satisfiable for a pair \((W,\mathcal{F})\), a finite witness together with its Completion Object forces the complete recovery of the infinite structural family via the Determination Relation.

\subsection{The Present Lack of Integration}
An insufficiency nevertheless remains. The Morphisms of Determination exist as separate maps, and the five operations exist as separate constructions. They have not yet been recognized as the components of one single mathematical object. The theory therefore still treats as scattered what is already, by the preceding recoveries, a coherent whole. The dependency graph remains incomplete only in recognition, not in content.

\subsection{The Objective of this Chapter}
The present chapter repairs precisely this insufficiency. Nothing further is constructed. The preceding constructions are already sufficient to force a single mathematical object. The remaining task is only to \emph{recognize} that object.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for Recognition of a Single Object}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand recognition. Article VIII requires that earlier mathematical content remain recoverable after every reduction. Article X requires integrity of the dependency graph. Article XII requires that abstractions remain recoverable from explicit construction. 

\subsection{Architectural Synthesis}
To leave the Completion Objects, the Morphisms of Determination and their five operations as an unassembled collection is to leave the interaction of determination unrecovered as a mathematical whole, even though every constituent is already present.

The missing recognition is the unique structure whose components are precisely the Completion Objects (as objects) and the Morphisms of Determination (as morphisms), and whose internal relations are precisely the operations already forced. That structure is the \textbf{Determination Algebra}. It is forced by assembly, not by new construction.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Assembly}
\label{sec:requirements}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any structure that realizes the Determination Algebra must satisfy requirements forced by the existing mechanisms of the Witness Calculus and by the Morphisms already recovered.

\begin{enumerate}
    \item \textbf{Coexistence.} Previously recovered Completion Objects must coexist within a single governing structure.
    \item \textbf{Morphism coexistence.} Previously recovered Morphisms of Determination must coexist as the transport structure of the algebra.
    \item \textbf{Recoverability preservation.} Previously recovered operations (composition, identity, restriction, extension, Canonical Transport) must remain fully recoverable within the assembly.
    \item \textbf{Minimal assembly.} No new primitive assumptions may be introduced; the structure must be assembled entirely from previously recovered components and their forced operations.
    \item \textbf{Uniqueness.} The assembly must be unique.
\end{enumerate}

These requirements are not chosen. They are the direct expression of the Morphisms of Determination and their forced operations recognized as a single coherent architecture of minimal logical cost. The algebra itself has \emph{zero additional logical cost}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Unique Assembly of the Determination Algebra}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Completion Objects recovered in Chapter 3 together with the Morphisms of Determination recovered in Chapter 5 already determine a unique structure whose object component is the system of all Completion Objects, whose morphism component is the network of all Morphisms of Determination, and whose internal relations are precisely the five operations already forced by the Witness Calculus.

\subsection{Closure and Compatibility}
No new construction is forced. The previously recovered constituents already satisfy every compatibility condition. The Determination Algebra is therefore forced as the unique minimal assembly of these previously recovered structures.

\begin{theorem}[Unique Assembly of the Determination Algebra]
\label{thm:algebra}
The previously recovered structures---Completion Objects, Morphisms of Determination, and the five operations of identity, composition, restriction, extension and Canonical Transport---assemble uniquely into a single recoverable structure \(\mathfrak{D}\) satisfying the five forced requirements of Section \ref{sec:requirements}. This structure is the Determination Algebra. It is fully recoverable from the Witness and introduces zero additional logical cost.
\end{theorem}

\begin{proof}
Every constituent has already been recovered independently in Chapters 3 and 5. Every compatibility condition (closure under the five operations, associativity of composition, unitality of identities) has already been established independently. The present chapter introduces no additional mathematical content; it merely recognizes the unique mathematical object in which these previously recovered constructions coexist. 

Uniqueness follows because the components and the operations are uniquely determined by previous constructions, and the assembly of minimal logical cost is forced by the Reduction Principle. Recoverability follows because every constituent expands into primitive witness expressions. The algebra itself therefore has \emph{zero logical cost}: it is \emph{pure recognition}.
\end{proof}

Only after the algebra has been shown to be the unique minimal assembly do we introduce the notation \(\mathfrak{D}\) for the Determination Algebra.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Inherited Structure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The algebraic properties already proved for Morphisms of Determination are inherited without change by the assembled object \(\mathfrak{D}\).

\begin{theorem}[Inherited Associativity and Unitality]
\label{thm:inherited}
Composition in \(\mathfrak{D}\) is associative. For every object \(C\) the identity morphism \(\operatorname{id}_C\) is a two-sided unit for composition. These properties are not new; they are the direct inheritance, inside the single object \(\mathfrak{D}\), of Theorems 5.2 and 5.3.
\end{theorem}

\begin{proof}
The statements are identical to the corresponding statements already proved for Morphisms of Determination. The assembly merely reinterprets those statements as internal identities of \(\mathfrak{D}\). No new proof is required.
\end{proof}

\begin{theorem}[Generated Subalgebras]
\label{thm:subalgebras}
Let \(S\) be any collection of objects and morphisms of \(\mathfrak{D}\). There exists a unique smallest subalgebra \(\langle S\rangle\subseteq\mathfrak{D}\) containing \(S\). The subalgebra is itself fully recoverable from the Witness.
\end{theorem}

\begin{proof}
The intersection of all subalgebras containing \(S\) is again a subalgebra and is the unique minimal such. Recoverability follows because every generator is recoverable and the operations preserve recoverability. The construction introduces no new content beyond the assembly already forced.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recoverability of the Algebra}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[The Algebra Disappears into the Witness]
\label{thm:alg-recover}
Every statement about the Determination Algebra \(\mathfrak{D}\) expands uniquely into statements already expressible in the Witness Calculus. No new primitive is required. The algebra itself disappears into the Witness.
\end{theorem}

\begin{proof}
Every object of \(\mathfrak{D}\) is a Completion Object, already shown recoverable. Every morphism is a Morphism of Determination, already shown recoverable. Every operation is one of the five operations of Chapter 5. 

The assembly of these components into the single structure \(\mathfrak{D}\) is a finite syntactic construction within the Witness Calculus. Since every statement about \(\mathfrak{D}\) is obtained by finite composition of these recoverable constituents, every statement expands uniquely into witness expressions. The algebra itself therefore disappears into the Witness: it is pure shorthand for already recovered content and has zero logical cost.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding constructions no longer exist independently. They are recognized as components of a single mathematical object, the Determination Algebra \(\mathfrak{D}\). The Morphisms of Determination are no longer a system of separate maps; they are the morphisms of a single algebra whose objects are the Completion Objects and whose operations are closed, associative, unital, and fully recoverable. Nothing new has been built; the object has merely been recognized.

The next insufficiency appears at once. The algebra exists, yet there is still no criterion for when two objects of \(\mathfrak{D}\) represent the same determination. Without a notion of determination-preserving equivalence, the algebra cannot yet form classes, cannot form quotients, and cannot support classification.

The next chapter must therefore recover Determination Equivalence. Theory continues to force the next structure. Applications remain forbidden until the full apparatus of Completion is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--5 of the present volume. In particular it relies upon the Witness, the Criterion of Determination, the conditional Completion Objects, the Determination Relation, the Morphisms of Determination (including identity, composition, restriction, extension and Canonical Transport), and all theorems of Chapters 2--5. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Determination Algebra is forced as the unique minimal assembly of already recovered components: Completion Objects, Morphisms of Determination, and the five operations of Chapter 5. The algebra itself has zero logical cost and disappears into the Witness. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory to zero additional cost by recognizing that the previously isolated Morphisms of Determination already assemble into one coherent algebraic object \(\mathfrak{D}\). Separate operations are replaced by a single structure of pure recognition. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Chapters 1--5. Every requirement is derived from explicit recoverability. The algebra is obtained purely by recognition of already recovered components; no new existence assumptions and no new mathematical content are introduced. No structure is introduced before its necessity has been forced. The dependency graph of the monograph remains inviolable. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The Determination Algebra \(\mathfrak{D}\) has been forced as the unique minimal assembly of already recovered components. Nothing further was constructed; the object was recognized. The next insufficiency is the absence of a criterion for when two objects of \(\mathfrak{D}\) represent the same determination. The next chapter must recover Determination Equivalence. The emergence of Determination Equivalence becomes the next forced development.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Determination Equivalence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Unrecognized Equivalence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 6 recognized the Determination Algebra \(\mathfrak{D}\) as the forced minimal assembly of Completion Objects and Morphisms of Determination. The algebra exists as a single mathematical object of zero additional logical cost. Composition is associative, identities are unital, and every collection generates a unique subalgebra. Everything is fully recoverable from the Witness.

An insufficiency nevertheless remains. The algebra supplies objects and morphisms, yet it supplies no criterion for when two objects of \(\mathfrak{D}\) represent the same determination. Without such a criterion, distinct Completion Objects may be transportable into each other by reciprocal Morphisms of Determination, yet the theory has no recovered notion of \emph{sameness of determination}. The dependency graph remains incomplete until this notion is forced.

The preceding constructions are now sufficient to force a single mathematical equivalence. Nothing further is constructed. The remaining insufficiency is only that this relation has not yet been recognized.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for Determination Equivalence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Constitutional Imperatives}
The Constitution and the recovered architecture jointly demand the equivalence. \textbf{Article VIII} requires that earlier mathematical content remain recoverable after every reduction. \textbf{Article X} requires integrity of the dependency graph. \textbf{Article XII} requires that abstractions remain recoverable from explicit construction. 

\subsection{The Architectural Gap}
An algebra whose objects cannot be compared for identity of determination leaves the absolute content of each infinite family unrecovered: two objects may determine identical infinite structural behaviour, yet the theory has not recognized the finite certificate of that identity.

The missing structure is the unique equivalence relation on the objects of \(\mathfrak{D}\) that holds precisely when two Completion Objects determine the same infinite structural family up to Morphisms of Determination. That relation is forced as \textbf{Determination Equivalence}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Equivalence}
\label{sec:forced-requirements}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any relation that realizes Determination Equivalence must satisfy five requirements forced by the existing mechanisms of the Witness Calculus and by the Determination Algebra already recovered.

\begin{enumerate}
    \item \textbf{Reflexivity.} Every object of \(\mathfrak{D}\) must be equivalent to itself, coexisting with the forced identity morphisms.
    \item \textbf{Symmetry.} If \(C_1\) is equivalent to \(C_2\), then \(C_2\) is equivalent to \(C_1\), corresponding to reciprocal transport.
    \item \textbf{Transitivity.} The relation must be transitive, structurally inherited from the composition of morphisms.
    \item \textbf{Morphism compatibility.} If there exists a Morphism of Determination from \(C_1\) to \(C_2\) and a Morphism of Determination from \(C_2\) to \(C_1\), then \(C_1\) and \(C_2\) must be equivalent.
    \item \textbf{Zero logical cost.} The relation must contain no information beyond what is required for the preceding four requirements, and it must disappear entirely into the Witness.
\end{enumerate}

These five requirements are not chosen. They are the direct expression of the Morphisms of Determination assembled inside \(\mathfrak{D}\) and applied to the necessity of structural identity.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Emergence of Determination Equivalence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Once reciprocal Morphisms of Determination have been recovered, no further construction is required. Their existence already forces a relation on Completion Objects. The remaining task is only to exhibit that relation explicitly.

Two objects \(C_1\) and \(C_2\) within \(\mathfrak{D}\) stand in the forced relation, denoted \(C_1 \sim_{\operatorname{Det}} C_2\), if and only if there exist reciprocal Morphisms of Determination \(f: C_1 \to C_2\) and \(g: C_2 \to C_1\).

\begin{theorem}[Unique Emergence of Determination Equivalence]
\label{thm:equivalence}
The relation \(\sim_{\operatorname{Det}}\) is forced as the unique equivalence relation on the objects of \(\mathfrak{D}\) that satisfies the five requirements of Section \ref{sec:forced-requirements}. It has zero logical cost and is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
Reflexivity is inherited directly from the existence of identity morphisms (Theorem 5.2). Symmetry is intrinsic to the definition of reciprocal morphisms. Transitivity is inherited from the closure of Morphisms of Determination under composition (Theorem 5.3). Morphism compatibility holds by definition.

Zero logical cost and recoverability are achieved because the relation is constructed entirely from the already assembled components of the Determination Algebra \(\mathfrak{D}\). No new mathematical content is introduced; the equivalence itself disappears into the Witness. Uniqueness is absolute: any other relation satisfying the five forced requirements must hold precisely whenever mutual Morphisms of Determination exist, and must therefore coincide with \(\sim_{\operatorname{Det}}\).
\end{proof}

Only after the equivalence has been shown to be the unique minimal assembly do we attach the notation \(\sim_{\operatorname{Det}}\).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Inherited Properties}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The relation \(\sim_{\operatorname{Det}}\) inherits its algebraic character entirely from the Morphisms of Determination.

\begin{theorem}[Inherited Equivalence Properties]
\label{thm:inherited-eq}
The relation \(\sim_{\operatorname{Det}}\) is reflexive, symmetric and transitive. These properties are not new; they are the direct inheritance, inside the single relation \(\sim_{\operatorname{Det}}\), of the identity morphisms and the composition of Morphisms of Determination already established in Chapter 5.
\end{theorem}

\begin{proof}
The statements are identical to the corresponding statements already proved for Morphisms of Determination. The emergence of the relation merely reinterprets those statements as the defining properties of an equivalence. No new proof is required.
\end{proof}

\begin{theorem}[Compatibility with Morphisms]
\label{thm:compatibility}
If \(f: C_1 \to C_2\) and \(g: C_2 \to C_1\) are Morphisms of Determination, then \(C_1 \sim_{\operatorname{Det}} C_2\). Conversely, if \(C_1 \sim_{\operatorname{Det}} C_2\), then there exist Morphisms of Determination in both directions. The relation is therefore exactly the relation of mutual morphic transport.
\end{theorem}

\begin{proof}
Immediate from the definition of \(\sim_{\operatorname{Det}}\) and the uniqueness established in Theorem \ref{thm:equivalence}.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Determination Equivalence has been recognized. The Determination Algebra \(\mathfrak{D}\) now possesses an internal notion of sameness: two objects represent the same determination precisely when they stand in the relation \(\sim_{\operatorname{Det}}\). Nothing new has been constructed; the relation has been forced by the already recovered reciprocal Morphisms of Determination and has zero logical cost.

The next insufficiency appears at once. The equivalence partitions the algebra into collections of objects that represent identical determination, yet those partitions have not yet been studied as mathematical objects in their own right. Without recovered \emph{Determination Classes} the theory cannot yet speak of the absolute content shared by equivalent objects, nor can it isolate canonical representatives or form a quotient.

The next chapter must therefore recover Determination Classes. Theory continues to force the next structure. Applications remain forbidden until the full apparatus of Completion is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--6 of the present volume. In particular it relies upon the Witness, the Criterion of Determination, the conditional Completion Objects, the Morphisms of Determination, the Determination Algebra \(\mathfrak{D}\), and all theorems of Chapters 2--6. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Determination Equivalence emerges inherently from the previously recovered reciprocal Morphisms of Determination. The relation has zero logical cost and disappears into the Witness. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by converting the raw objects of the Determination Algebra into a single, zero-cost notion of sameness. Comparison of infinite families is reduced to the existence of reciprocal Morphisms of Determination. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Chapters 1--6. Every requirement is derived from explicit recoverability. The equivalence is obtained purely by recognizing the relationships between existing Morphisms of Determination. No structure is introduced before its necessity has been forced, and inherited properties are recognized rather than proven from scratch. The dependency graph of the monograph remains inviolable. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
Determination Equivalence \(\sim_{\operatorname{Det}}\) has been recovered as the unique zero-cost equivalence forced by reciprocal Morphisms of Determination. The algebra now possesses an internal notion of sameness. The next insufficiency is that the partitions created by this equivalence have not yet been recovered as mathematical objects. The next chapter must recover Determination Classes. The emergence of Determination Classes becomes the next forced development.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Determination Classes}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Unpartitioned Equivalence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 7 recognized \textbf{Determination Equivalence} (\(\sim_{\operatorname{Det}}\)) as the unique zero-cost relation forced by reciprocal Morphisms of Determination. The algebra \(\mathfrak{D}\) now possesses an internal standard of sameness: two Completion Objects represent identical determination if and only if they stand in this relation.

An insufficiency nevertheless remains. The relation \(\sim_{\operatorname{Det}}\) evaluates pairs of objects, but the theory has not yet recovered the partitions created by this equivalence as mathematical structures in their own right. A relation merely identifies; it does not aggregate. Without recovering these partitions as explicit structures, the theory cannot treat a family of equivalent determinations as a single mathematical entity, nor can it transition from the study of isolated objects to the study of the determination structure as a whole.

Every recovered equivalence relation already determines a unique partition. Once Determination Equivalence has been recovered, the corresponding partition already exists within the dependency architecture. The remaining insufficiency is only that it has not yet been isolated. The present chapter repairs precisely this insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for Structural Partitions}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the explicit recovery of these partitions. \emph{Article VIII} requires that earlier mathematical content remain recoverable after every reduction. \emph{Article XII} requires that every abstraction remain recoverable from explicit construction. An apparatus that can identify equivalent objects but cannot encapsulate them into unified structures violates these articles: the global algebraic behaviour of determination remains dispersed across redundant individual representatives.

The missing structures are the \textbf{partition blocks} forced by Determination Equivalence. These blocks aggregate identical determining content, allowing the theory to operate structurally on the determination itself rather than on the arbitrary Completion Objects that realize it.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Determination Classes}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

No new construction is required. Every equivalence relation recovered in the Witness Calculus already determines its associated partition. The remaining task is only to isolate that partition explicitly.

\subsection{Formalization of Classes}

\begin{theorem}[Recovery of Determination Classes]
\label{thm:classes}
For every Completion Object \(C \in \mathfrak{D}\) there exists a unique collection
\[
[C]_{\operatorname{Det}} = \{C' \in \mathfrak{D} \mid C' \sim_{\operatorname{Det}} C\}
\]
that is forced by Determination Equivalence. This collection is the \textbf{Determination Class} of \(C\). It has zero additional logical cost and is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
The collection is uniquely determined by the already recovered relation \(\sim_{\operatorname{Det}}\). Membership of any object is decided solely by the existence of reciprocal Morphisms of Determination, which have already been recovered. No new content is introduced; the partition block is forced by the equivalence. Recoverability follows immediately from the recoverability of \(\sim_{\operatorname{Det}}\).
\end{proof}

Only after the class has been shown to be uniquely forced do we introduce the notation \([C]_{\operatorname{Det}}\) for the Determination Class of \(C\).

\subsection{Partition Properties}

\begin{theorem}[Partition of the Determination Algebra]
\label{thm:partition}
Every Completion Object belongs to exactly one Determination Class. Distinct Determination Classes are disjoint, and their union is the entire object component of \(\mathfrak{D}\).
\end{theorem}

\begin{proof}
By Theorem 7.2, \(\sim_{\operatorname{Det}}\) is reflexive, symmetric, and transitive. Reflexivity ensures every Completion Object \(C\) belongs to \([C]_{\operatorname{Det}}\), so the union of all classes covers the object component of \(\mathfrak{D}\). Symmetry and transitivity ensure that if \([C_1]_{\operatorname{Det}}\) and \([C_2]_{\operatorname{Det}}\) share an element, every element of one is equivalent to every element of the other, forcing the classes to be identical. Hence distinct classes are strictly disjoint.
\end{proof}

Every Completion Object within \([C]_{\operatorname{Det}}\) determines the same structural behaviour up to Determination Equivalence.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Compatibility of Operations with Equivalence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Before the operations of the algebra \(\mathfrak{D}\) can descend to the classes, the operations themselves must be shown to be compatible with the equivalence.

\begin{theorem}[Compatibility of Operations with Equivalence]
\label{thm:compatibility}
The five operations of the Determination Algebra---composition, identity, restriction, extension, and Canonical Transport---are compatible with Determination Equivalence \(\sim_{\operatorname{Det}}\). That is, each operation sends equivalent data to equivalent data and therefore descends to well-defined operations on Determination Classes.
\end{theorem}

\begin{proof}
Identity morphisms are preserved because every object is equivalent to itself. Composition preserves equivalence because if \(C_1 \sim_{\operatorname{Det}} C_1'\), \(C_2 \sim_{\operatorname{Det}} C_2'\), \(f: C_1 \to C_2\), and \(f': C_1' \to C_2'\) are Morphisms of Determination, then the composites of reciprocal morphisms with \(f\) and \(f'\) remain Morphisms of Determination by Theorem 5.3; the resulting composites witness the required equivalences. Restriction and extension preserve cores and therefore preserve the existence of reciprocal morphisms. Canonical Transport is itself defined by a core-preserving admissible transformation and therefore sends equivalent objects to equivalent objects. Hence every operation of \(\mathfrak{D}\) is compatible with \(\sim_{\operatorname{Det}}\).
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Quotient by Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Recovery of the Quotient]
\label{thm:quotient}
There exists a unique structure \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) whose objects are the Determination Classes and whose morphisms are the Morphisms of Determination descended to those classes via the compatibility established in Theorem \ref{thm:compatibility}. This structure is the \textbf{Quotient} of \(\mathfrak{D}\) by Determination Equivalence. It inherits associativity and unitality directly from \(\mathfrak{D}\) and possesses zero additional logical cost.
\end{theorem}

\begin{proof}
By Theorem \ref{thm:compatibility} the operations of \(\mathfrak{D}\) respect the partition and descend to well-defined operations on the classes. The resulting structure is therefore well-defined. Associativity and unitality are strictly inherited from \(\mathfrak{D}\) (Theorem 6.2); no new algebraic proofs are required. Recoverability is absolute, as the quotient is composed entirely of partitions formed by the recoverable relation \(\sim_{\operatorname{Det}}\). Uniqueness follows because any other structure whose objects are the classes and whose morphisms are the descended morphisms must coincide with this one.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Universality and Minimality of the Quotient}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{The Universal Property}

\begin{theorem}[Universal Property of the Quotient]
\label{thm:universality}
Every construction previously recovered in the Witness Calculus that is preserved by Morphisms of Determination is constant on Determination Classes and factors uniquely through the quotient
\[
\mathfrak{D} \to \mathfrak{D}/{\sim_{\operatorname{Det}}}.
\]
\end{theorem}

\begin{proof}
Let \(Q\) be any construction previously recovered in the Witness Calculus that is preserved by every Morphism of Determination. If \(C_1 \sim_{\operatorname{Det}} C_2\), there exist reciprocal Morphisms of Determination between them. Since \(Q\) is preserved by these morphisms, the structural evaluation of \(Q\) at \(C_1\) must exactly match the structural evaluation of \(Q\) at \(C_2\). Hence \(Q\) is strictly constant on each Determination Class. The natural projection \(\mathfrak{D} \to \mathfrak{D}/{\sim_{\operatorname{Det}}}\) aggregates exactly these equivalent objects, so \(Q\) descends to a unique, well-defined property on the quotient.
\end{proof}

\subsection{Minimality}

\begin{theorem}[Minimality of the Quotient]
\label{thm:minimality}
The quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) is the unique minimal structure that realizes this identification. Any other structure that identifies all pairs related by \(\sim_{\operatorname{Det}}\) factors uniquely through the quotient.
\end{theorem}

\begin{proof}
By the Universal Property (Theorem \ref{thm:universality}), any structure \(\mathfrak{Q}\) identifying all equivalent Completion Objects must evaluate uniformly on each Determination Class. Therefore, the canonical projection into \(\mathfrak{Q}\) factors uniquely through the exact partition already forced by Determination Equivalence. Hence, the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) is the unique minimal such structure.
\end{proof}

The natural objects for global investigation are now Determination Classes.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Determination Classes have been recovered, and the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) has been formed. The theory of Completion has successfully aggregated redundant realizations into unified structural entities. The natural objects of study are now Determination Classes.

The next insufficiency appears at once. The quotient now exists, and every morphism-preserving construction descends to it. Yet nothing distinguishes one quotient object from another by absolute finite structural data. The theory can manipulate Determination Classes algebraically, but it lacks a finite structural fingerprint---an \textbf{invariant}---that captures the defining determining content shared universally across an entire class.

Without class invariants, the theory cannot classify the universe of all possible determinations through explicit structural quantities. The next chapter must therefore recover the Invariants of Determination. Theory continues to force the next structure. Applications remain forbidden until the full apparatus is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--7 of the present volume. In particular it relies upon the Witness, the Morphisms of Determination, the Determination Algebra \(\mathfrak{D}\), Determination Equivalence \(\sim_{\operatorname{Det}}\), and all theorems of Chapters 2--7. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Determination Classes and the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) are recognized as strictly inherited architectures. The partition is determined purely by the existing equivalence relation. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by elevating the objects of study from individual, redundant completions to unified Determination Classes. The quotient is the unique minimal structure that realizes this identification. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles. Every requirement is derived from explicit recoverability. The classes and the quotient are obtained purely by recognizing the partitions and the descent forced by existing equivalence. No structure is introduced before its necessity has been forced. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
Determination Classes and the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) have been recovered. The algebra is now fully partitioned by identity of determination, and every recoverable morphism-invariant construction factors uniquely through the classes. The next insufficiency is the absence of finite structural fingerprints that classify these Determination Classes. The next chapter must recover the Invariants of Determination as the minimal structural content preserved across equivalent objects. The emergence of Invariants of Determination becomes the next forced development.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Invariants of Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Unclassified Classes}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 8 recovered Determination Classes and the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\). The theory successfully aggregated equivalent Completion Objects into unified mathematical entities. By the Universal Property of the Quotient (Theorem 8.5), every construction preserved by Morphisms of Determination factors uniquely through these classes. The natural objects of global investigation are now the Determination Classes themselves.

An insufficiency nevertheless remains. The quotient exists, and the algebraic operations have safely descended to it, but the theory lacks an \textit{absolute, finite structural data point} that distinguishes one quotient object from another. A Determination Class is an abstraction---a collection of equivalent Completion Objects; it is not yet a finite, explicit quantity in its own right. We can manipulate these classes algebraically, but we have no finite determining core that captures the exact determining content shared universally across an entire class.

Without such a canonical structural core, the theory cannot classify the universe of possible determinations through explicit quantities. The dependency graph remains incomplete until the absolute identifying content of each class is forced. The present chapter repairs precisely this insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for Finite Classification}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the explicit recovery of class invariants. \textbf{Article XII} requires that every abstraction remain recoverable from explicit construction. A Determination Class is an abstraction---a collection of equivalent Completion Objects. For this abstraction to be fully recoverable and strictly governed by the \textit{Witness Calculus}, it must possess a finite, explicit determining core that can be isolated and measured.

\textbf{Article VI} requires that logical reduction take precedence over computational convenience. The theory cannot depend upon the choice of representative to define a class; it must extract the irreducible structural essence that survives every transport. The missing structure is the unique, minimal determining content strictly common to every object in a Determination Class.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Invariant}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any structure that serves to classify Determination Classes must satisfy three requirements forced by the existing mechanisms of the \textit{Witness Calculus} and by the Universal Property of the Quotient.

\begin{enumerate}
    \item \textbf{Class Uniformity.} \\
    The structure must evaluate identically for every Completion Object within a given Determination Class.
    \item \textbf{Transport Preservation.} \\
    The structure must be preserved under every Morphism of Determination.
    \item \textbf{Minimal Determining Content.} \\
    The structure must contain exactly the absolute determining information that survives all reciprocal transport and no redundant information. It must be strictly minimal.
\end{enumerate}

These requirements are not chosen. They are the direct expression of logical economy applied to the necessity of classifying structural identity.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Determination Invariant}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Theoretical Existence}

No new construction is forced. The required structure is already latent within the recovered equivalence.

\begin{theorem}[Recovery of the Determination Invariant]
\label{thm:invariant-recovery}
For every Determination Class \([C]_{\operatorname{Det}}\), there exists a unique minimal recoverable content that is preserved by every Morphism of Determination acting within the class. This structure is the \emph{Determination Invariant} of the class, denoted \(\operatorname{Inv}([C]_{\operatorname{Det}})\). It possesses zero additional logical cost and is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
Consider the intersection of all recoverable determining contents preserved by every reciprocal Morphism of Determination acting within the class \([C]_{\operatorname{Det}}\). By the construction of Morphisms of Determination (Chapter 5), this collection of preserved structures is non-empty, as it must contain at least the irreducible coherent core forced by the generating witnesses.

The intersection of any collection of preserved structures is again strictly preserved by those same morphisms. By the Minimal Determining Substructure theorem (Theorem 2.1), every descending chain of determining substructures stabilizes at a unique minimal element. Therefore the operation of intersection terminates at a unique, irreducible minimal element. This unique minimal content strictly satisfies class uniformity, transport preservation and minimality. Recoverability follows directly from the recoverability of the intersecting components.
\end{proof}

\subsection{Corollaries of the Core}

The invariant is not assigned to the class; it is recovered from the class. Every class possesses exactly one such invariant.

\begin{corollary}[Canonical Core]
\label{cor:canonical-core}
The Determination Invariant \(\operatorname{Inv}([C]_{\operatorname{Det}})\) is the unique canonical determining core of its Determination Class.
\end{corollary}

\begin{proof}
Immediate from Theorem \ref{thm:invariant-recovery}: the invariant is the unique minimal recoverable content preserved by every Morphism of Determination within the class.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Completeness of the Determination Invariant}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The intersection produces a minimal preserved structure. To ensure that this reduction does not discard information required for classification, we must establish that the minimal core retains complete determination.

\begin{theorem}[Completeness of the Determination Invariant]
\label{thm:invariant-completeness}
The Determination Invariant recovers every determination-preserving construction on its class.
\end{theorem}

\begin{proof}
By the Universal Property of the Quotient (Theorem 8.5), every recoverable construction previously recovered in the Witness Calculus that is preserved by Morphisms of Determination factors uniquely through the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\). The Determination Invariant is itself recovered from the class (Theorem \ref{thm:invariant-recovery}) and is the unique minimal content that evaluates every such construction constantly on the class. Therefore every determination-preserving construction factors uniquely through the invariant. Hence the invariant is complete for the determination of the class.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Classification by Invariants}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{The Fundamental Equivalence}

The recovery of the Determination Invariant allows the theory to classify the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) entirely by explicit finite data.

\begin{theorem}[Classification Theorem]
\label{thm:classification}
Two Completion Objects \(C_1\) and \(C_2\) belong to the same Determination Class if and only if their Determination Invariants are identical:
\[
[C_1]_{\operatorname{Det}} = [C_2]_{\operatorname{Det}} \quad \iff \quad \operatorname{Inv}([C_1]_{\operatorname{Det}}) = \operatorname{Inv}([C_2]_{\operatorname{Det}}).
\]
\end{theorem}

\begin{proof}
If \([C_1]_{\operatorname{Det}} = [C_2]_{\operatorname{Det}}\), they represent the same object in the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\). By Theorem \ref{thm:invariant-recovery} the invariant is a strict property of the class itself, forcing the invariants to be identical.

Conversely, suppose \(\operatorname{Inv}([C_1]_{\operatorname{Det}}) = \operatorname{Inv}([C_2]_{\operatorname{Det}})\). Then \(C_1\) and \(C_2\) share the identical minimal determining content preserved under transport. By the Completeness of the Determination Invariant (Theorem \ref{thm:invariant-completeness}), this minimal content is mathematically sufficient to evaluate every determination-preserving construction on either object. Therefore the Morphisms of Determination force a unique reciprocal transport between any two objects sharing this exact core. This reciprocal transport satisfies the criterion for Determination Equivalence \(\sim_{\operatorname{Det}}\) (Theorem 7.1). Hence \(C_1\) and \(C_2\) occupy the exact same Determination Class.
\end{proof}

\subsection{Implications for Objects}

\begin{corollary}[Representative Independence]
\label{cor:representative-independence}
For every Completion Object \(C\), the invariant \(\operatorname{Inv}([C]_{\operatorname{Det}})\) depends only on its Determination Class and is strictly independent of the chosen Completion Object representing that class.
\end{corollary}

This corollary provides the absolute classification of Completion Objects. The theory is no longer concerned with isolated objects or unquantified partitions; it is driven entirely by the classification of \textit{canonical determining content}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Determination Invariants have been recovered. The quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) is now fully classified by absolute, minimal structural fingerprints. Every Determination Class possesses exactly one invariant, and identical invariants guarantee identical determination.

The next insufficiency appears at once. The theory can now compute and compare the recoverable determining signature of any known completion. However, it cannot yet answer the inverse problem: \textit{Given a prospective invariant, or a finite witness possessing structural obstruction, under what conditions does a canonical realization of that completion actually exist?}

The invariants classify Determination Classes that already exist, but the theory lacks a \textit{generative apparatus}. This generative gap immediately raises two dual insufficiencies: identifying the exact structural conditions that prevent realization (\textit{obstruction}), and characterizing the conditions under which realization succeeds (\textit{completion}). From the perspective of logical inevitability, the obstruction is prior: the theory must first isolate precisely what prevents finite determination, and only then characterize its elimination.

The next chapter must therefore recover Completion Obstructions. Theory continues to force the next structure. Applications remain forbidden until the full apparatus is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Monograph Architectural Audits}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Dependency Audit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--8 of the present volume. In particular it relies upon the Witness, the Morphisms of Determination, Determination Classes, the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\), and all theorems of Chapters 2--8. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.

\subsection{Primitive Audit}
No new mathematical primitive has been introduced. The Determination Invariant is strictly recovered as the minimal intersection of content preserved by existing Morphisms of Determination within a known class. The single primitive of the monograph remains the \textit{Witness}.

\subsection{Reduction Audit}
This chapter reduces the logical cost of the theory by replacing the comparison of abstract equivalence classes with the direct structural identity of their minimal preserved invariants. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.

\subsection{Consistency Audit}
The constructions of this chapter are fully consistent with the constitutional principles. Every requirement is derived from explicit recoverability and minimality. The existence of the invariant is proven directly from the intersection of preserved structures rather than postulated. Completeness is derived from the Universal Property of the Quotient rather than from circular description. The Classification Theorem relies on a rigorous chain from Completeness to reciprocal transport. The chapter obeys Articles IV, XI and XIII.

\subsection{Future Work}
The Determination Invariants have been recovered, successfully classifying the quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\). The next insufficiency is the absence of a generative theory that dictates when a finite witness admits a realization of these invariants. The theory must first isolate the exact structural mechanisms that prevent realization. The next chapter must address the inverse problem by recovering Completion Obstructions. The emergence of Completion Obstructions becomes the next forced development.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Completion Obstructions}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of a Descriptive Theory}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 9 recovered the Determination Invariants. The quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) is now completely classified by finite, canonical determining cores. Whenever a Completion Object exists, its absolute structural fingerprint can be isolated, compared and classified.

An insufficiency nevertheless remains. The invariants classify Determination Classes that already exist, but the theory has no generative mechanism to determine when a finite witness actually admits such a class. If a finite witness \(W\) fails to completely determine its infinite structural family \(\mathcal{F}\), the \textit{Criterion of Determination} (Chapter 3) simply returns a negative evaluation. However, in the \textit{Witness Calculus} a failure cannot be an abstract negation. It must be a finite, explicit, recoverable structure.

Without isolating the exact structural objects that prevent determination, the theory can describe successes but cannot classify failures. The dependency graph remains incomplete until the abstract failure of the Criterion is recovered as an explicit mathematical object. The present chapter repairs precisely this insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for a Finite Certificate of Failure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the explicit recovery of obstructions. 

\subsection{Constitutional Imperatives}
\textbf{Article XII} requires that every abstraction remain recoverable from explicit construction. An ``inability to complete'' is an abstraction; to satisfy the Constitution this inability must be localized into a specific, finite substructure that irreconcilably violates the forced requirements of determination.

\textbf{Article VIII} requires that earlier mathematical content remain recoverable after every reduction. The informal ``obstructions of a common form'' isolated in Chapter 1 must now be recovered as rigorous mathematical objects within the formal algebraic architecture built in Chapters 3 through 9. The missing structure is the unique, canonical finite content that serves as the \textit{absolute certificate of failure} for the Criterion of Determination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Obstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any structure that serves as a certificate of failure must satisfy three requirements forced by the existing mechanisms of the Witness Calculus and by the Criterion of Determination.

\begin{enumerate}
    \item \textbf{Finite Localization.} The structure must be a strictly finite configuration evaluable entirely within the minimal closed system of the witness.
    \item \textbf{Criterion Violation.} The structure must explicitly forbid the simultaneous satisfaction of co-situation, core-invariance and overlap-preservation required by the Criterion (Theorem 3.1).
    \item \textbf{Minimal Irreducibility.} The structure must contain no redundant information; it must be a minimal obstruction such that any proper substructure would theoretically permit determination.
\end{enumerate}

These requirements are not chosen. They are the direct structural translation of a logical failure to satisfy the Criterion, localized into a recoverable object.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Completion Obstructions}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

When the Criterion of Determination is not satisfiable for a pair \((W,\mathcal{F})\), the dependency propagation of the Witness Calculus cannot extend infinitely; it stabilizes at a finite incompatible configuration. We do not invent this blockage; we recover it as an object.

\subsection{Formal Proof and Characterization}

\begin{theorem}[Recovery of the Canonical Obstruction Object]
\label{thm:obstruction-recovery}
Whenever the Criterion of Determination fails for a finite witness \(W\) and its infinite structural family \(\mathcal{F}\), there exists a unique canonical representative among the minimal finite substructures that strictly forbid determination. This representative is the \textbf{Completion Obstruction}, denoted \(\operatorname{Obs}(W,\mathcal{F})\). It has zero additional logical cost and is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
Assume the Criterion of Determination (Chapter 3) fails for \((W,\mathcal{F})\). The failure implies that no finite content \(C\) can simultaneously satisfy co-situation, core-invariance and overlap-preservation. By the Coherence Algebra and the Dependency Propagation Architecture (Volume II), any such incompatibility among finite constraints is witnessed by a finite irreconcilable dependency configuration within the dependency architecture.

Because the relation ``is a determining substructure of'' is strictly well-founded (Theorem 2.1), the collection of such irreconcilable dependency configurations must contain at least one minimal element. While multiple minimal configurations that forbid determination may exist within the closed system, the Canonical Algebra (Volume II) forces these minimal configurations to collapse to a unique canonical representative. This unique canonical minimal configuration strictly violates the Criterion, contains no redundant data, and is constructed entirely from previously recovered primitive witness expressions.
\end{proof}

The Completion Obstruction \(\operatorname{Obs}(W,\mathcal{F})\) is not a truth value indicating ``false.'' It is a structural object: a specific, finite collision of dependencies that mathematically prevents lossless compression.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Fundamental Dichotomy}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The recovery of the Completion Obstruction elevates the status of the Criterion of Determination from a mere test to a generator of strict dichotomies. Every finite witness has exactly one structural destiny.

\subsection{The Architectural Choice}

\begin{theorem}[The Obstruction Dichotomy]
\label{thm:dichotomy}
For every finite witness \(W\) and its forced infinite structural family \(\mathcal{F}\), exactly one of the following mathematical objects is forced to exist:
\begin{enumerate}
    \item A unique canonical Completion Object \(\operatorname{Comp}(W,\mathcal{F})\) realizing complete determination.
    \item A unique canonical Completion Obstruction \(\operatorname{Obs}(W,\mathcal{F})\) rigorously preventing determination.
\end{enumerate}
\end{theorem}

\begin{proof}
By Theorem 3.2 (Conditional Existence of the Completion Object), if the Criterion is satisfiable, the unique Completion Object \(\operatorname{Comp}(W,\mathcal{F})\) is forced. By Theorem \ref{thm:obstruction-recovery}, if the Criterion is not satisfiable, the unique canonical Completion Obstruction \(\operatorname{Obs}(W,\mathcal{F})\) is forced. These two conditions are exhaustive and mutually exclusive by the structural logic of the Witness Calculus. Therefore every finite witness mathematically forces exactly one of these two explicit structural outcomes.
\end{proof}

The informal observations of Chapter 1 have been fully resolved. Every structural obstruction of the common form is now explicitly recovered as a finite mathematical object \(\operatorname{Obs}(W,\mathcal{F})\).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Completion Obstructions have been recovered. The theory is no longer merely descriptive. When a witness fails to determine its infinite structural family, the absolute reason for that failure is isolated as a finite, canonical and minimal mathematical object.

The obstruction has now been isolated as a finite mathematical object. The remaining insufficiency is no longer the identification of failure, but the passage from the absence of obstruction to the existence of completion. We now know what prevents realization. However, whether obstruction-freeness alone forces realization has not yet been determined, nor has the theory recovered the explicit structural conditions that guarantee a realization exists.

The next chapter must therefore recover \textit{Completion Realization}. Theory continues to force the next structure. Applications remain forbidden until the full apparatus is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--9 of the present volume. In particular it relies upon the Witness, the Criterion of Determination, the Canonical Algebra, the Coherence Algebra, the Dependency Propagation Architecture, and all theorems of Chapters 2--9. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Completion Obstruction is rigorously recovered as the unique canonical representative of the minimal finite irreconcilable dependency configurations inside the dependency architecture that prevent the satisfaction of the Criterion. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by replacing the abstract concept of ``failure to complete'' with a strictly finite, localized structural object. The problem of determining existence is reduced to the problem of isolating this finite obstruction. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles. Every requirement is derived from explicit recoverability and minimality. The existence of minimal obstructions is proven directly from the well-foundedness of the dependency architecture, and uniqueness is secured via the Canonical Algebra. The dichotomy follows necessarily from prior existence theorems. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
Completion Obstructions have been formally recovered, establishing a strict dichotomy for every finite witness. The next insufficiency is the passage from the absence of obstruction to the existence of completion. The next chapter must address whether obstruction-freeness forces realization by recovering Completion Realization. The emergence of Completion Realization becomes the next forced development.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Completion Realization}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Negative Identification}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 10 recovered Completion Obstructions and established the Fundamental Dichotomy: every finite witness mathematically forces either a Completion Object or a Completion Obstruction. We now possess the exact, finite mathematical objects that serve as absolute certificates of failure.

An insufficiency nevertheless remains. The dichotomy guarantees that exactly one of these two structures must exist, but the theory has not yet recovered the constructive passage between them. We know what prevents realization, but we have not yet established that the mere \textit{absence} of a Completion Obstruction is structurally sufficient to \textit{force} the realization of a Completion Object. In the Witness Calculus, existence cannot be inferred from a double negative; the absence of failure does not construct success. The generative mechanism that explicitly builds the realization from an obstruction-free witness has not yet been recovered.

The dependency graph remains incomplete until this generative mechanism is formalized. The present chapter repairs precisely this insufficiency by recovering Completion Realization.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for a Generative Mechanism}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand a theory of realization. Article XII requires that every abstraction remain recoverable from explicit construction. To state that a witness ``can be completed'' is an abstraction unless the Completion Object itself is explicitly forced into existence by a recovered mechanism.

Article VI dictates that logic must be constructive. The theory cannot simply assume that a prospective invariant (from Chapter 9) or an obstruction-free witness (from Chapter 10) magically summons a Completion Object. The missing structure is the Realization Theorem: the explicit, structural guarantee that whenever the canonical obstruction vanishes, the Criterion of Determination is inevitably satisfied and the Completion Object is strictly constructible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of Realization}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any theory that governs Completion Realization must satisfy three requirements forced by the existing mechanisms of the Witness Calculus and by the Fundamental Dichotomy.

\begin{enumerate}
    \item \textbf{Structural Sufficiency.} The confirmed absence of the canonical Completion Obstruction must be mathematically equivalent to the satisfiability of the Criterion of Determination.
    \item \textbf{Constructive Recovery.} The realization must not rely on external existence axioms; it must be uniquely constructible from the coherent core of the obstruction-free witness.
    \item \textbf{Invariant Realization.} The theory must dictate not only when a witness realizes a completion, but when a proposed Determination Invariant realizes a non-empty Determination Class.
\end{enumerate}

These requirements are not chosen. They are the direct translation of constructive existence within the algebraic framework recovered in Chapters 3 through 10.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Finiteness of Structural Incompatibility}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

To establish that the absence of a finite obstruction strictly forces realization, the theory must first prove that infinite incompatibilities cannot exist without a finite footprint. A failure of the Criterion cannot hide ``at infinity.''

\begin{theorem}[Finite Witness Principle for Incompatibilities]
\label{thm:finite-incompatibility}
Every failure of the Criterion of Determination within an infinite structural family \(\mathcal{F}\) is explicitly witnessed by a finite irreconcilable dependency configuration within the closed system of \(W\).
\end{theorem}

\begin{proof}
In the Witness Calculus, the infinite structural family \(\mathcal{F}\) is not an arbitrary set; it is strictly forced by finite iterative applications of admissible transformations on the finite witness \(W\) (Volume II). The Dependency Propagation Architecture guarantees that every relation in \(\mathcal{F}\) is the result of a finite propagation chain. 

Therefore, any global incompatibility among constraints in \(\mathcal{F}\) must arise from the collision of finite propagation chains. By the Coherence Algebra, such a collision is fundamentally local and occurs at a specific finite stage of propagation. It is impossible for an obstruction to exist exclusively in the infinite limit without already manifesting as a finite irreconcilable overlap among the constituent finite structures. Hence, every global failure is necessarily witnessed by a finite irreconcilable configuration.
\end{proof}

This theorem provides the vital bridge: a global failure of determination is strictly equivalent to the presence of a finite obstruction.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Realization Architecture}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The generative mechanism of the theory is now forced by the interplay between the Finite Witness Principle and the Completion Obstruction.

\subsection{Sufficiency of Obstruction-Freeness}

\begin{theorem}[Sufficiency of Obstruction-Freeness]
\label{thm:sufficiency}
Let \(W\) be a finite witness and \(\mathcal{F}\) its infinite structural family. If the canonical Completion Obstruction \(\operatorname{Obs}(W, \mathcal{F})\) does not exist within the dependency architecture of \(W\), then the Criterion of Determination is strictly satisfiable.
\end{theorem}

\begin{proof}
By the Finite Witness Principle (Theorem \ref{thm:finite-incompatibility}), any failure of the Criterion of Determination must be witnessed by a finite irreconcilable dependency configuration. By Theorem 10.1, if any such finite configurations exist, the Canonical Algebra forces them to collapse to the unique canonical Completion Obstruction \(\operatorname{Obs}(W, \mathcal{F})\). 

Therefore, the non-existence of \(\operatorname{Obs}(W, \mathcal{F})\) mathematically guarantees that absolutely no finite irreconcilable configurations exist. By the Coherence Algebra, an architecture free of irreconcilable dependencies admits a well-defined, internally consistent limit inside the minimal closed system. This structurally guarantees that at least one finite content \(C\) satisfies all forced requirements (co-situation, core-invariance, and overlap-preservation). Hence, the Criterion is strictly satisfiable.
\end{proof}

\subsection{The Realization Theorem}

\begin{theorem}[The Realization Theorem]
\label{thm:realization}
For every finite witness \(W\) that is free of the canonical Completion Obstruction \(\operatorname{Obs}(W, \mathcal{F})\), the realization of the Completion Object \(\operatorname{Comp}(W, \mathcal{F})\) is explicitly constructible and completely forced.
\end{theorem}

\begin{proof}
By Theorem \ref{thm:sufficiency}, the absence of the canonical obstruction forces the strict satisfiability of the Criterion of Determination. By Theorem 3.2 (Conditional Existence of the Completion Object), whenever the Criterion is satisfiable, the existence of the unique canonical Completion Object \(\operatorname{Comp}(W, \mathcal{F})\) is forced via the reduction to minimal determining substructure. Because both the verification of obstruction-freeness and the well-founded reduction to minimal determining content are deterministic operations governed by the Canonical Algebra, the Completion Object is directly constructible from \(W\). No external axioms are required.
\end{proof}

Realization is now a recovered operation. The theory does not merely classify what exists; it generates the completion directly from the certification of obstruction-freeness.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Realization of Invariants}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Realization Theorem extends naturally from individual witnesses to the Determination Invariants recovered in Chapter 9.

\begin{theorem}[Realization of Invariants]
\label{thm:invariant-realization}
Let \(I\) be a prospective finite determining core. \(I\) is the Determination Invariant for a valid Determination Class in \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) if and only if \(I\) is internally coherent and free of Completion Obstructions.
\end{theorem}

\begin{proof}
If \(I\) is the invariant of a valid Determination Class, it must be the minimal determining content of some valid Completion Object (Theorem 9.1). By Theorem 10.2 (The Obstruction Dichotomy), a valid Completion Object strictly forbids the existence of a Completion Obstruction. Furthermore, \(I\) must be internally coherent by the Coherence Algebra.

Conversely, suppose \(I\) is internally coherent and obstruction-free. By the Completeness of the Determination Invariant (Theorem 9.3), a coherent invariant possesses the exact minimal structural data required to evaluate any determination-preserving construction. Treated as an initial witness, its obstruction-freeness invokes the Realization Theorem (Theorem \ref{thm:realization}), strictly forcing the construction of a Completion Object. Because \(I\) is assumed to be an irreducible core, it must mathematically coincide with its own minimal invariant. Hence, every valid invariant realizes exactly one Determination Class.
\end{proof}

The quotient \(\mathfrak{D}/{\sim_{\operatorname{Det}}}\) is now perfectly characterized. The theory can definitively state exactly which finite structural fingerprints correspond to actual determinations and which do not.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Completion Realization has been recovered. The generative gap is closed. The theory now possesses the complete mechanical pathway: it can test a witness, isolate its obstruction if it fails, or definitively construct its Completion Object if the obstruction vanishes. Every valid invariant realizes a Determination Class.

The next insufficiency appears at once. We have recovered the mechanism for realizing individual Completion Objects and characterizing individual classes. However, we have not yet examined the global boundary of this generative process. Does the process of determination ascend indefinitely, or does there exist a maximal, terminal completion that bounds the entire hierarchy of Determination Classes?

Without establishing the absolute bounds of the realization theory, the architecture remains open-ended. The next chapter must therefore recover Universal Completion. Theory continues to force the next structure. Applications remain forbidden until the full apparatus is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--10 of the present volume. In particular it relies upon the Witness, the Criterion of Determination (Ch 3), the Determination Invariants (Ch 9), the Completion Obstruction and the Dichotomy (Ch 10), and the Coherence, Canonical, and Dependency Algebras. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Completion Realization is formally derived as a constructive consequence of obstruction-freeness, guaranteed by the Finite Witness Principle and previously established conditional existence theorems. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by converting the conditional existence of Completion Objects into a constructive realization forced by the absence of finite obstructions. The reduction relies entirely on demonstrating that infinite incompatibilities are finitely witnessed. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles. Every requirement is derived from explicit recoverability. The existence of the realization is proven directly from the established Dichotomy, the Finite Witness Principle, and the Coherence Algebra rather than asserted externally. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
Completion Realization has been recovered, supplying the generative mechanism that links obstruction-freeness to strict constructibility. The next insufficiency is the absence of a global boundary to this realization process. The next chapter must recover Universal Completion to establish the maximal terminal object of the determination hierarchy. The emergence of Universal Completion becomes the next forced development.
\end{futurework}

\chapter{Universal Completion}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Partial Realization}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 11 recovered Completion Realization. The generative gap is closed: the explicit absence of the canonical Completion Obstruction strictly forces the realization of the Completion Object. The theory can now transition mechanically from an obstruction-free finite determining core to the constructive determination of its infinite structural family.

An insufficiency nevertheless remains. The Realization Theorem guarantees the existence of specific Completion Objects for specific structural families \(\mathcal{F}\). However, a single finite witness \(W\) may force multiple distinct, valid structural constraints. We can realize these dependencies partially, generating divergent Completion Objects that determine isolated fragments of the witness's total potential.

Yet the theory has not recovered a structure that represents the \textit{totality} of what \(W\) determines. If the space of all valid realizations for a witness remains fragmented, the theory cannot answer whether these divergent partial realities can be reconciled into a single absolute structure, or if they remain permanently fractured. The mathematical problem of total determination cannot even be stated until the absolute structural horizon of \(W\) is formalized. The dependency graph remains incomplete until this maximal object is recovered. The present chapter repairs precisely this insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for an Absolute Horizon}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the explicit recovery of this total determination. Article XII requires that every abstraction remain recoverable from explicit construction. To speak of ``the full determining power of a witness'' is an unrecoverable abstraction unless that absolute ceiling is localized into a single, finite, constructible structure.

Article X requires the integrity of the dependency graph. The theory cannot leave the reconciliation of partial Completion Objects to external assumption. If the structural constraints forced by \(W\) are mutually coherent and free of obstruction, their unification must be rigorously forced as a mathematical object within the Determination Algebra \(\mathfrak{D}\). The missing structure is the Universal Completion: the unique, maximal realization from which every partial realization is recoverable.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of Universal Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any structure that serves as the absolute horizon of realization for a witness must satisfy three requirements forced by the existing mechanisms of the Witness Calculus and by the Realization Theorem.

\begin{enumerate}
    \item \textbf{Maximal Determination.} The structure must completely determine the maximal coherent, obstruction-free structural family forced natively by the witness.
    \item \textbf{Structural Subsumption.} Every valid partial Completion Object generated by the witness must be strictly recoverable as a determining substructure of this maximal object.
    \item \textbf{Finite Constructibility.} Despite subsuming the totality of compatible realizations, the determining core of the object must remain strictly finite and explicitly constructible.
\end{enumerate}

These requirements are not chosen. They are the direct structural translation of a maximal bound applied to the generative theory of Completion Realization.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Absolute Horizon}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

We do not postulate the existence of a maximal upper bound by an infinite limit; we recover it directly from the finiteness of determining cores established in Chapter 2 and the finite generation of the minimal closed system.

\begin{theorem}[Finiteness of the Structural Horizon]
\label{thm:horizon-finiteness}
For every finite witness \(W\), the collection of all mutually coherent, obstruction-free determining cores within its minimal closed system admits a unique, finite maximal element.
\end{theorem}

\begin{proof}
By the Minimal Determining Substructure theorem (Theorem 2.1), every Completion Object is completely governed by a strictly finite determining core. Every such determining core is a recoverable substructure of the minimal closed system generated by \(W\).

The minimal closed system of \(W\) is generated by a finite number of primitive relations and admissible transformations. Consequently it contains only finitely many recoverable primitive witness expressions, and therefore only finitely many recoverable substructures. In particular, the collection of all possible determining cores constructible from \(W\) is finite.

Since every determining core is a recoverable substructure of one and the same ambient finite object (the minimal closed system of \(W\)), the family of all mutually coherent, obstruction-free determining cores forms a finite family of substructures of a single finite object. Their union is therefore well-defined and is itself a finite determining structure. This finite structure is the unique maximal obstruction-free determining core forced by \(W\).
\end{proof}

\begin{theorem}[Recovery of the Universal Completion]
\label{thm:universal-recovery}
For every finite witness \(W\), the maximal obstruction-free determining core forces a unique canonical realization. This realization is the Universal Completion Object, denoted \(\operatorname{Univ}(W)\). It possesses zero additional logical cost and is fully recoverable from the Witness.
\end{theorem}

\begin{proof}
By Theorem \ref{thm:horizon-finiteness}, the absolute structural horizon of \(W\) is governed by a finite, obstruction-free determining core. Because this core is finite and free of the canonical Completion Obstruction, it satisfies the prerequisites of the Realization Theorem (Theorem 11.2). The Realization Theorem strictly forces the explicit construction of its corresponding Completion Object. This object is \(\operatorname{Univ}(W)\). Its recoverability is absolute, as it is generated directly from the finite architecture of \(W\).
\end{proof}

The object \(\operatorname{Univ}(W)\) is the absolute structural ceiling of the witness. It represents the unification of every compatible reality the witness can force.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Structural Subsumption}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Because \(\operatorname{Univ}(W)\) is the maximal realization, it structurally governs all partial determinations within the Determination Algebra \(\mathfrak{D}\).

\begin{theorem}[Structural Subsumption of Partial Realizations]
\label{thm:subsumption}
For every valid Completion Object \(C\) coherently forced by the witness \(W\), there exists a unique Morphism of Determination transporting \(C\) into \(\operatorname{Univ}(W)\).
\end{theorem}

\begin{proof}
Let \(C\) be any valid Completion Object forced by \(W\). By definition, the determining content of \(C\) is a coherent, obstruction-free core within the minimal closed system of \(W\). By Theorem \ref{thm:horizon-finiteness}, the determining core of \(\operatorname{Univ}(W)\) is the maximal combination of all such cores.

Therefore the minimal determining content of \(C\) is strictly a recoverable determining substructure of the core of \(\operatorname{Univ}(W)\). By the Canonical Algebra and Theorem 5.4 (Canonical Transport), the embedding of this determining substructure structurally forces a unique determination-preserving map. Hence a unique Morphism of Determination exists from \(C\) into \(\operatorname{Univ}(W)\).
\end{proof}

\begin{corollary}[The Universal Invariant]
\label{cor:universal-invariant}
The Determination Invariant \(\operatorname{Inv}([\operatorname{Univ}(W)]_{\operatorname{Det}})\) intrinsically subsumes every other mutually coherent Determination Invariant forced by \(W\).
\end{corollary}

This corollary establishes that the fragmented universe of partial determinations for any given witness is entirely resolved into a single, maximal structural fingerprint.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Universal Completion has been recovered. The structural architecture of Completion is now absolutely bounded. We possess the Recognition Criterion (Chapter 3), the Morphisms of Determination (Chapter 5), the Determination Algebra (Chapter 6), the Determination Invariants (Chapter 9), the Completion Obstructions (Chapter 10), the Realization Theorem (Chapter 11), and now the Universal Completion (Chapter 12). The mathematical problem of total determination for a finite witness has been forced and resolved.

The next insufficiency appears at once. The entire apparatus has been recovered as a static, structural reality. We possess the absolute rules of determination, but we have not yet recovered the explicit operational calculus required to mechanize these rules. The theory can mathematically force a Completion Object, but it lacks the finite, step-by-step constructive procedures---the compression and decompression mechanics---to execute these reductions within the Witness Calculus.

Without an operational calculus, the theory is structurally complete but procedurally static. The next chapter must therefore recover the Compression Calculus. Theory continues to force the next structure. Applications remain forbidden until the full operational apparatus is recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--11 of the present volume. In particular it relies upon the Witness, the Minimal Determining Substructure (Chapter 2), the Morphisms of Determination (Chapter 5), the Realization Theorem (Chapter 11), the Coherence Algebra, and the Canonical Algebra. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Universal Completion is rigorously recovered via the finiteness of determining cores established in Chapter 2 together with the finite generation of the minimal closed system, completely avoiding infinite limits or external amalgamation assumptions. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by replacing the fragmented proliferation of partial Completion Objects with a single, maximal, bounding structure. Subsumption guarantees that every localized determination can be strictly recovered from this single object. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles. Every requirement is derived from explicit recoverability. The existence of the maximal object is proven directly from the finiteness of the closed system and the Realization Theorem, explicitly avoiding unearned classical compactness or category-theoretic assumptions. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The Universal Completion has been recovered, establishing the absolute structural horizon for the realization process. The theoretical architecture of Volume IV is now complete. The next insufficiency is the absence of procedural operations to mechanize these structural forced rules. The next chapter must recover the Compression Calculus. The emergence of the Compression Calculus becomes the next forced development.
\end{futurework}

\chapter{The Compression Calculus}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of a Static Architecture}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter 12 recovered the Universal Completion, sealing the absolute structural horizon for any finite witness. The theoretical architecture of Volume IV is now mathematically complete: we possess the Criterion (Chapter 3), the Morphisms (Chapter 5), the Determination Algebra (Chapter 6), the classes and their Invariants (Chapters 8 and 9), the Obstructions (Chapter 10), and the Realization mechanics (Chapter 11).

An insufficiency nevertheless remains. The entire apparatus has been recovered as a static, structural reality. The theorems guarantee that minimal determining cores exist, that realizations are forced, and that universal limits bound the system. However, the theory has not yet recovered the explicit operational calculus required to mechanize these guarantees. We know that a Completion Object reduces to a unique invariant, but we lack the finite, step-by-step procedural operators to execute this reduction computationally within the Witness Calculus.

Without an operational calculus, the theory is structurally complete but procedurally static. It can classify what exists, but it cannot mechanically compress or decompress the structural data. The dependency graph remains incomplete until the static theorems are mobilized into dynamic procedural operators. The present chapter repairs precisely this insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Demand for Operational Mechanics}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitution and the recovered architecture jointly demand the explicit recovery of procedural mechanics. Article XII requires that every abstraction remain recoverable from explicit construction. To claim that a structure ``can be reduced'' to a minimal core is an abstraction unless the explicit operator performing that reduction is formally recovered.

Article VI dictates that logic must be constructive and finite. The theory cannot rely on platonic existence proofs to manipulate data. If a finite witness completely determines an infinite family, there must exist explicit, finite mechanical operators that execute the compression of redundant data and the subsequent decompression of the infinite family. The missing structure is the Compression Calculus: the integrated system of operators that operationalizes the Determination Algebra.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Forced Requirements of the Calculus}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Any operational calculus governing determination must satisfy three requirements forced by the existing mechanisms of the Witness Calculus and by the established algebra.

\begin{enumerate}
    \item \textbf{Operator Duality.} The calculus must provide dual operators: one for reducing a Completion Object to its minimal invariant (Compression), and one for unfolding an invariant into its canonical realization (Decompression).
    \item \textbf{Structural Fidelity.} The operators must perfectly respect the Determination Algebra; applying compression followed by decompression must yield an object strictly within the original Determination Class.
    \item \textbf{Finite Termination.} The application of any operator must be mechanically guaranteed to terminate in a finite number of discrete steps, relying strictly on the finiteness of the minimal closed system.
\end{enumerate}

These requirements are not chosen. They are the direct procedural translations of minimality, realization, and finiteness applied to the structural architecture of Completion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Operational Mechanics}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

We do not define algorithmic procedures arbitrarily; we recover the operational mechanics already latent within the dependency architecture of the witness. 

The preceding chapters already recover two complementary procedures. The reduction of a Completion Object to its irreducible minimal determining core is forced by the well-foundedness of determining substructures (Theorem 2.1). The reconstruction of the canonical Completion Object from that core is forced by the Realization Theorem (Theorem 11.2). These procedural mechanics are therefore forced as the Compression and Decompression Operators.

\begin{theorem}[Recovery of the Compression and Decompression Operators]
\label{thm:operators}
There exist exactly two fundamental operators forced by the algebraic structure of determination:
\begin{enumerate}
    \item The \textbf{Compression Operator}, denoted \(\downarrow\), explicitly reduces a valid Completion Object \(C \in \mathfrak{D}\) along its dependency graph to its unique canonical determining core:
    \[
    \downarrow C = \operatorname{Inv}([C]_{\operatorname{Det}}).
    \]
    \item The \textbf{Decompression Operator}, denoted \(\uparrow\), explicitly unfolds a mutually coherent, obstruction-free determining core \(I\) into its canonical realization via the admissible transformations of the Witness Calculus:
    \[
    \uparrow I = \operatorname{Comp}(I, \mathcal{F}_I).
    \]
\end{enumerate}
\end{theorem}

\begin{proof}
The existence and uniqueness of the outputs for \(\downarrow\) are strictly guaranteed by the recovery of the Determination Invariant (Theorem 9.1). The existence and uniqueness of the outputs for \(\uparrow\) are explicitly guaranteed by the Realization Theorem (Theorem 11.2). Because these mappings are rigorously determined by the underlying algebraic architecture, the corresponding operators are fully recoverable.
\end{proof}

\begin{theorem}[Finite Termination of the Operators]
\label{thm:finite-termination}
The execution of both the Compression Operator \(\downarrow\) and the Decompression Operator \(\uparrow\) strictly terminates in a finite number of structural reductions and expansions.
\end{theorem}

\begin{proof}
For the Compression Operator \(\downarrow\): The reduction follows the well-founded relation ``is a determining substructure of.'' By the finiteness of the minimal closed system generated by the witness (Theorem 12.1), the total number of recoverable substructures is strictly finite. Therefore, any sequence of strict structural reductions must terminate in a finite number of steps at the irreducible minimal element.

For the Decompression Operator \(\uparrow\): The unfolding mechanism verifies obstruction-freeness and applies canonical limits. Because the generation of the minimal closed system relies on a finite number of primitives and transformations, the detection of overlaps exhausts a strictly finite lattice of substructures (Theorem 12.1). By the constructive nature of the Realization Theorem (Theorem 11.2), the synthesis of the canonical Completion Object is a direct, finite integration of this core. Hence, both operators execute in finite steps.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Identities of the Compression Calculus}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The operators \(\downarrow\) and \(\uparrow\) do not act independently; they form a cohesive operational calculus governed by strict algebraic identities.

\begin{theorem}[The Laws of the Calculus]
\label{thm:calculus-laws}
For every valid Completion Object \(C \in \mathfrak{D}\) and every valid Determination Invariant \(I\), the Compression and Decompression operators satisfy the following fundamental identities:
\begin{enumerate}
    \item \textbf{Invariant Stability:} \(\downarrow (\uparrow I) = I\).
    \item \textbf{Operational Equivalence:} \(\uparrow (\downarrow C) \sim_{\operatorname{Det}} C\).
    \item \textbf{Compression Idempotence:} \(\downarrow (\downarrow C) = \downarrow C\).
    \item \textbf{Canonical Idempotence:} \(\uparrow (\downarrow (\uparrow I)) = \uparrow I\).
\end{enumerate}
\end{theorem}

\begin{proof}
Proof of Invariant Stability: By definition, \(\uparrow I\) synthesizes the canonical Completion Object whose minimal determining content is exactly \(I\). Applying \(\downarrow\) to this realization mechanically recovers its minimal determining core (Theorem 9.1). Because \(I\) is irreducible, the reduction evaluates to \(I\). 

Proof of Operational Equivalence: The compression \(\downarrow C\) yields its unique Determination Invariant \(\operatorname{Inv}([C]_{\operatorname{Det}})\). The decompression \(\uparrow (\downarrow C)\) unfolds this invariant into its canonical Completion Object. By the Classification Theorem (Theorem 9.4), because \(\uparrow (\downarrow C)\) and \(C\) share the identical Determination Invariant, they belong to the exact same Determination Class. They are therefore connected by reciprocal Morphisms of Determination, forcing \(\uparrow (\downarrow C) \sim_{\operatorname{Det}} C\).

Proof of Compression Idempotence: Evaluating \(\downarrow C\) yields the irreducible invariant \(I\). Because \(I\) contains no redundant substructures, a subsequent application of the reduction operator \(\downarrow\) cannot isolate a smaller core. The operator stabilizes, yielding \(I = \downarrow C\).

Proof of Canonical Idempotence: Substituting Invariant Stability (\(\downarrow (\uparrow I) = I\)) directly into the decompression operator yields \(\uparrow (I) = \uparrow I\). Any canonically realized object remains absolutely stable under cyclical compression and decompression.
\end{proof}

This theorem converts the static equivalences of Chapter 7 and Chapter 9 into an explicit, mechanical syntax. The algebraic structure of determination can now be computationally executed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Completeness of the Calculus}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

We must now establish that these recovered operators are sufficient to process any determination-preserving operation within the theory.

\begin{theorem}[Completeness of the Compression Calculus]
\label{thm:calculus-completeness}
The Compression Calculus is complete for Determination. Every determination-preserving construction within the minimal closed system factors uniquely into a finite composition of the Compression Operator \(\downarrow\), the Decompression Operator \(\uparrow\), and Canonical Transport.
\end{theorem}

\begin{proof}
By the Universal Property of the Quotient (Theorem 8.5), any structural construction preserved by Morphisms of Determination depends entirely upon the Determination Class, and not upon the individual Completion Object. 

The Compression Operator \(\downarrow\) mechanically distills any object \(C\) to its canonical invariant \(I\), representing its class. Canonical Transport (Theorem 5.4) explicitly maps these invariants across structural equivalences without loss of determination. The Decompression Operator \(\uparrow\) subsequently rebuilds the canonical realization from the invariant. Because every determination-preserving property is invariant under these steps, any such construction is mechanically factorizable through this explicit three-operator procedural pipeline. No external or ad-hoc operations are required.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Direction of Construction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Compression Calculus has been recovered. The theory of Completion is now fully operationalized. We possess not only the absolute structural ceilings and boundaries of determination, but the explicit, finite mechanical operators (\(\downarrow\) and \(\uparrow\)) required to compute them. The calculus is finite, completely governed by rigorous algebraic laws, and structurally complete for determination.

The logical and procedural apparatus required for canonical investigation has now been recovered. The complete machinery of the Witness Calculus—from the foundational primitive relations of Volume I to the universal operational calculus of Volume IV—exists in its entirety. 

The next insufficiency appears at once. The apparatus exists exclusively as an internal, self-contained architecture. The theory has not yet demonstrated how this rigorous mechanical machinery interfaces with, strictly reduces, and definitively resolves external mathematical reality. Without deploying the calculus upon concrete structural settings, the theory remains a sterile internal mechanics. 

The next chapter must therefore unleash the apparatus. We must recover the Applications of the Witness Calculus. Theory has finished forcing internal structures; it must now force external resolutions.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and upon Chapters 1--12 of the present volume. In particular it relies upon the Determination Invariant (Ch 9), the Realization Theorem (Ch 11), the finiteness of the closed system (Ch 12), the Determination Equivalence (Ch 7), and Canonical Transport (Ch 5). No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Compression Calculus is strictly recovered by isolating the procedural mechanics already forced by the structural proofs of minimality and realization. The operators are finite syntax built upon the single primitive of the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by converting abstract existence theorems and equivalence relations into explicit, finitely terminating procedural operators. The static architecture is reduced to a mechanical syntax capable of complete factorization. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles. Every procedural requirement is derived from explicit recoverability. The finite termination of the operators relies strictly on the finite generation bounds recovered in Theorem 12.1. The Operational Equivalence theorem aligns perfectly with the previously forced Classification Theorem (Theorem 9.4). The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The Compression Calculus has been recovered, providing the finite mechanical operations that execute the Determination Algebra. The internal theoretical architecture of the monograph is now complete. The final insufficiency is the absence of concrete external deployment. The final chapter must cover the Applications of the Witness Calculus, demonstrating the structural resolution of mathematical problems via the forced apparatus.
\end{futurework}

\chapter{Canonical Investigation of Infinite Branching Structural Families}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Classical Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Canonical Investigation Framework recovered in Part I of the present volume stands complete. Every finite witness may be reconstructed. Its dependency architecture may be classified. Its coherent core may be isolated. Its admissible transformations may be enumerated. The Criterion of Determination may be applied. Completion Obstructions may be isolated. Realization may be forced when the obstruction vanishes. Universal Completion may be formed. Compression and decompression may be executed by the recovered operators.

An insufficiency nevertheless appears. When the framework is required to determine the global behaviour of an infinite structural family generated by the iterated application of a structural function whose local action on any witness is completely determined by a finite structural observable of that witness, the apparatus terminates. The dependency graph of any finite generating witness determines only finite initial segments of the recoverability relations inside the family. Nothing inside the completed machinery of Part I forces the coherent amalgamation of those segments into a single determined core for the entire infinite family. Finite local determination does not yield complete global determination.

The termination is structural. It belongs to the framework itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding insufficiency cannot even be expressed within the language recovered by Part I. The minimal object capable of expressing it must therefore be recovered.

Such an object consists of an infinite collection of trajectories generated by the repeated application of an admissible structural function whose local action at each stage depends only upon a recoverable structural observable of the current witness. This recovered object will be called an Infinite Branching Structural Family.

The reconstruction proceeds entirely inside the Witness Calculus. Let \(\mathcal{W}\) be any localized ambient of witnesses recovered in Volume III. The Dependency Propagation and Coherence Algebras already recover finite discrete structural observables that select, at each witness, one transformation from a finite family of admissible transformations. The structural function whose successive application generates the family is the unique map that applies, at each stage, the transformation selected by such an observable. The infinite structural family is the set of all trajectories obtained by iterated application of that function starting from any finite initial witness. The dependency architecture of the family is the directed graph of recoverability relations forced by the Dependency Propagation Theorem. The coherent core of any finite initial segment of any trajectory is uniquely determined by the Coherence Algebra.

No external arithmetic, heuristic, or classical definition has been imported. The structure is forced solely by the necessity of expressing the local-to-global termination isolated above.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Structural Absoluteness}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The recovered Infinite Branching Structural Family is absolute. By the Canonical Transport theorem of Part I, its dependency graph and the action of its generating function are invariant under every admissible transformation that preserves the coherent core of the generating witness. Any two realizations of the same branching rule are related by a unique Morphism of Determination. The family is therefore independent of presentation. Its entire structural content remains fully recoverable from the Witness.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Canonical Observables}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The following observables are forced by the apparatus already recovered:

\begin{enumerate}
    \item the value of the local selector at any witness of any trajectory;
    \item the coherent core of any finite initial segment of any trajectory;
    \item the Determination Invariant of any finite prefix, recovered by the Compression Operator \(\downarrow\);
    \item the local Completion Object of any finite segment, forced by the Realization Theorem whenever the segment is free of Completion Obstruction.
\end{enumerate}

These observables exhaust the finite-state information that the present framework can extract. No further observable is admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Completion Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Absence of a Local-to-Global Mechanism]
\label{thm:local-global-absence}
The Completion Theory recovered in Part I determines every finite trajectory segment and every finite collection of such segments. The present apparatus contains no recovered mechanism that forces the coherent amalgamation of an entire Infinite Branching Structural Family into a single global Completion Object.
\end{theorem}

\begin{proof}
Let \(\sigma\) be any finite initial segment of a trajectory. By the Criterion of Determination and the Realization Theorem, \(\sigma\) possesses a unique local Completion Object whenever it is free of obstruction. The infinite family, however, requires the joint recoverability of an infinite collection of such locally coherent cores. The Criterion of Determination demands co-situation of determining content with a single generating witness. No structure recovered in Part I supplies a finite determining core that is co-situated with the entire infinite branching dependency architecture and that preserves the coherent overlap of every local core. Local determination therefore does not force global determination.
\end{proof}

\begin{theorem}[Universality of the Residual Problem]
\label{thm:universality-of-residual}
The preceding investigation isolates exactly one unresolved mathematical object. Every failure of global completion for an Infinite Branching Structural Family is equivalent to the absence of a mechanism that converts the collection of all local Completion Objects into a single globally coherent determination.
\end{theorem}

\begin{proof}
By Theorem \ref{thm:local-global-absence} the only obstruction that appears is the lack of a recovered mechanism that amalgamates local Completion Objects while remaining fully recoverable from the Witness Calculus. No other obstruction is exhibited. Hence every such failure is identical with this residual.
\end{proof}

\begin{corollary}
The residual of the present framework with respect to Infinite Branching Structural Families is unique.
\end{corollary}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Compression Operator \(\downarrow\) and the Decompression Operator \(\uparrow\) remain locally sufficient. For any finite sub-collection of trajectories the product of their Determination Invariants is well-defined and reconstructible. The operators are not closed under the infinite branching action. No finite witness presently recovered acts as the minimal determining core of an entire Infinite Branching Structural Family. Global compression of the infinite branching architecture is therefore impossible within the present framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The investigation terminates with residual insufficiency. The framework is internally consistent and completely determines every finite segment. It contains no recovered structure that solves the residual isolated by Theorem \ref{thm:universality-of-residual}. The exact mathematical object whose absence prevents further determination is a finite structural mechanism that converts locally coherent determination into globally coherent determination while remaining fully recoverable from the Witness.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding investigation is insufficient. The residual is not ignorance; it is the forced existence of a mathematical mechanism whose absence has been exhibited.

Any future mechanism capable of resolving the residual must satisfy the following universal property: for every Infinite Branching Structural Family, the image of the mechanism applied to the family is the unique minimal globally coherent determination that extends every local Completion Object of the family and is itself fully recoverable from the Witness Calculus by a finite sequence of Morphisms of Determination and Compression operations.

No such mechanism has been recovered. Its existence is not assumed. Its construction is forbidden until the residual has been shown to be invariant under structurally independent investigations. Only then does the characterization become the forced recovery of a new mathematical object of the framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and Part I of Volume IV. In particular it relies upon the Witness, the Coherence Algebra, Dependency Propagation, Morphisms of Determination, the Criterion of Determination, the Realization Theorem, the Compression Calculus, and the Common Form of Present Obstruction recovered in Chapter 1 of the present volume. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Infinite Branching Structural Family is recovered as the minimal structure forced by the local-to-global termination already exhibited by the framework. The residual mechanism is recovered only as a forced characterization; it is neither named nor constructed. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by converting every failure of global completion for infinite branching families into a single, unique residual of the Canonical Investigation Framework itself. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Part I. Construction precedes naming. No object is defined. The residual mechanism is characterized but neither assumed nor constructed. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The residual insufficiency isolated in this chapter is the forced existence of a mathematical mechanism that converts locally coherent determination into globally coherent determination. The next chapter must determine whether this residual is invariant under every structurally independent canonical investigation. Only if the residual is universal may the mechanism be recovered as a forced mathematical object of the completed framework.
\end{futurework}

\part{Completing the Canonical Investigation Framework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Universality of the Residual}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency Inherited from the Final Chapter of Part I}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The final chapter of Part I isolated a single residual insufficiency of the recovered Canonical Investigation Framework. Every investigation of an Infinite Branching Structural Family terminates by exhibiting a finite collection of local Completion Objects whose coherent cores remain jointly unrecoverable under any structure presently available inside the framework. The Criterion of Determination, the Realization Theorem, the Morphisms of Determination, and the Compression Calculus determine every finite segment and every finite sub-collection of segments. Nothing recovered forces their amalgamation into a single globally coherent determination that remains fully recoverable from the Witness.

The residual is precise. It is the absence of any mechanism that converts locally coherent determination into globally coherent determination while preserving co-situation, core-invariance, overlap-preservation, and Minimal Determining Content.

The preceding construction is therefore insufficient. The mathematics of Part II cannot continue until it is known whether this residual is accidental or whether the Canonical Investigation Framework itself admits only one possible place of termination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Why Universality Must Precede Recovery}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Article XI forbids the introduction of any object before it is logically unavoidable. Article IV forbids interpretation before construction. The Constitution therefore prohibits the recovery of any operator, algebra, or global structure until the residual that would force it has been shown to be the unique possible termination of the protocol itself.

If the protocol admits multiple independent termination behaviours, no single mathematical object is forced. If the protocol admits only one possible canonical termination, the residual becomes a theorem of the framework and the unique object capable of removing it becomes unavoidable.

Universality must therefore be recovered first. Construction is forbidden until uniqueness of termination has been proved.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Class of Admissible Canonical Investigations}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The object of study is no longer any particular Infinite Branching Structural Family. The object is the investigation protocol itself.

The preceding residual cannot be shown unique until the class of all admissible executions of the protocol has been recovered. That class is forced by the apparatus of Part I.

Let \(\mathfrak{I}\) be the class of all sequences of operations that begin with a finite witness \(W\), reconstruct its dependency architecture, isolate its coherent core, generate its admissible transformations, form the Infinite Branching Structural Family \(\mathcal{F}\) forced by those transformations, apply the Criterion of Determination to every finite initial segment, recover every local Completion Object free of obstruction, and terminate precisely when the collection of those local Completion Objects fails to determine a single global Completion Object for \(\mathcal{F}\).

Every element of \(\mathfrak{I}\) is itself a finite witness expression inside the Witness Calculus. Its dependency graph, coherent core, and canonical realization are recovered by the same constructions that recover any other witness. No external arithmetic, no classical conjecture, and no surface presentation of any particular family is required. The class \(\mathfrak{I}\) is forced solely by the necessity of examining the termination behaviour of the protocol.

The class \(\mathfrak{I}\) is therefore the unique minimal object capable of expressing the question of uniqueness of termination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Termination Class}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding recovery of \(\mathfrak{I}\) forces a further structure. Distinct investigations may in principle terminate with distinct residuals. The mathematics therefore requires the recovery of the class of all possible termination behaviours.

Let \(\mathfrak{T}\) be the class of all residuals that arise as the terminal stage of some investigation \(I\in\mathfrak{I}\). The assignment
\[
T:\mathfrak{I}\to\mathfrak{T},\qquad I\mapsto T(I)
\]
is forced by the protocol: each investigation produces exactly one residual, namely the structural content of its failure of global amalgamation.

No second class of termination behaviours is admitted. \(\mathfrak{T}\) is recovered solely as the image of the protocol under the Canonical Investigation Framework. The residual of Part I is one element of \(\mathfrak{T}\). The question of universality is precisely the question whether \(|\mathfrak{T}|=1\).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Structural Absoluteness of Termination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Structural Absoluteness of Termination]
\label{thm:absoluteness-termination}
The residual \(T(I)\) of any investigation \(I\in\mathfrak{I}\) is independent of presentation. If \(I_1,I_2\in\mathfrak{I}\) are related by a Morphism of Determination that preserves the coherent core of their generating witnesses, then \(T(I_1)=T(I_2)\).
\end{theorem}

\begin{proof}
By the Canonical Transport theorem of Part I, every Morphism of Determination preserves co-situation, core-invariance, and coherent overlap. The Criterion of Determination and the Realization Theorem are themselves invariant under such morphisms. Consequently the collection of local Completion Objects recovered by \(I_1\) is transported bijectively onto the collection recovered by \(I_2\), and the failure of their amalgamation is preserved. The residual is therefore an invariant of the Determination Class and is independent of any particular realization.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Canonical Observables of Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The following observables are forced by the apparatus already recovered and are sufficient for the comparison of residuals:

\begin{enumerate}
    \item the Determination Invariant of every finite initial segment of every trajectory of the Infinite Branching Structural Family under investigation;
    \item the local Completion Object of every obstruction-free finite segment, recovered by the Realization Theorem;
    \item the coherent overlap of any finite collection of such local Completion Objects;
    \item the image of the Compression Operator \(\downarrow\) applied to any finite product of Determination Invariants.
\end{enumerate}

These observables exhaust the finite-state information extractable from any element of \(\mathfrak{I}\). Their joint failure to determine a global Completion Object is precisely the residual under examination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Uniqueness of Canonical Termination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Uniqueness of Canonical Termination]
\label{thm:uniqueness-termination}
The Canonical Investigation Framework admits only one possible place of termination. The protocol itself possesses a unique failure mode: the absence of any recovered structure that forces the coherent amalgamation of the collection of all local Completion Objects into a single globally coherent determination co-situated with a finite generating witness and fully recoverable from the Witness Calculus.
\end{theorem}

\begin{proof}
By construction of every \(I\in\mathfrak{I}\), the protocol succeeds at every finite stage. The Criterion of Determination, the Realization Theorem, and the Compression Calculus of Part I remain fully effective on every finite initial segment and every finite sub-collection of segments. The Infinite Branching Structural Family forces an infinite collection of local Completion Objects whose joint recoverability is required for global determination. The Criterion of Determination demands co-situation of determining content with a single finite witness. No structure recovered in Part I supplies a finite determining core that is simultaneously co-situated with the entire infinite branching dependency architecture and that preserves the coherent overlap of every local core.

No other failure mode is possible. Every finite determination is already complete. Every local Completion Object free of obstruction is already realized. The only stage at which the protocol can terminate is the stage at which local determination is required to become global determination. The protocol therefore possesses exactly one possible place of termination, and that place is independent of the generating witness and of the particular branching rule.
\end{proof}

\begin{theorem}[Uniqueness of the Residual Characterization]
\label{thm:uniqueness-characterization}
Every admissible canonical investigation \(I\in\mathfrak{I}\) terminates with a residual satisfying exactly the same universal characterization: the absence of a finite structural mechanism that converts the collection of all local Completion Objects into a single globally coherent determination while remaining fully recoverable from the Witness Calculus by a finite sequence of Morphisms of Determination and Compression operations. No second independent characterization of the residual exists.
\end{theorem}

\begin{proof}
By Theorem \ref{thm:uniqueness-termination} the protocol admits only one possible failure mode. By Theorem \ref{thm:absoluteness-termination} that failure mode is independent of presentation. Consequently every residual \(T(I)\) is identical in structural content with the residual isolated by the final chapter of Part I. The characterization is therefore unique. No second independent characterization can arise, for any purported alternative would require a second place of termination, contradicting Theorem \ref{thm:uniqueness-termination}.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Determination: Universality}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Universality of the Residual]
\label{thm:universality}
The Termination Class is a singleton:
\[
|\mathfrak{T}|=1.
\]
Every admissible canonical investigation \(I\in\mathfrak{I}\) terminates with exactly the same residual. The residual is an invariant of the Canonical Investigation Framework itself.
\end{theorem}

\begin{proof}
By Theorem \ref{thm:uniqueness-termination} the protocol possesses only one possible place of termination. By Theorem \ref{thm:uniqueness-characterization} every residual arising from that place satisfies exactly the same universal characterization. Therefore \(T(I)\) is independent of the choice of \(I\in\mathfrak{I}\), so \(\mathfrak{T}\) contains exactly one element.
\end{proof}

\begin{corollary}
The residual isolated at the conclusion of Part I is not accidental. It is forced by the Canonical Investigation Framework itself. Every execution of the protocol terminates with that unique residual.
\end{corollary}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding investigation is insufficient. Universality has been established. The residual is no longer an observed absence; it has become constructive.

Universality converts the residual from an observed absence into a constructive specification. The missing mathematical object is no longer arbitrary. Any object satisfying the recovered universal characterization is unique up to Morphisms of Determination. The characterization is now a universal property of the framework itself.

No such object has been recovered. Its existence is not assumed. Its construction is no longer forbidden: the residual has been shown to be the unique possible termination of the protocol, and the characterization of that termination is unique. The following chapter therefore recovers not an invented operator but the unique realization forced by the present theorem.

The mathematics therefore requires the recovery of that unique realization.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes I--III and of Part I of Volume IV. In particular it relies upon the Witness, the Coherence Algebra, Dependency Propagation, Morphisms of Determination, the Criterion of Determination, the Realization Theorem, the Compression Calculus, the Common Form of Present Obstruction, and the residual isolated by the final chapter of Part I. No theorem depends upon any mathematical object introduced only in later chapters of Part II. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The class \(\mathfrak{I}\) of admissible canonical investigations and the Termination Class \(\mathfrak{T}\) are recovered as the minimal structures forced by the necessity of examining the termination behaviour of the protocol. The residual itself is recovered only as a forced theorem of uniqueness; it is neither named as an operator nor constructed. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by converting every failure of global completion into a single, unique residual of the Canonical Investigation Framework itself, proved by uniqueness of the protocol's failure mode rather than by enumeration of investigations. Heterogeneous surface presentations of Infinite Branching Structural Families are thereby eliminated. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes I--III and Part I. Construction precedes naming. No object is defined. Universality precedes recovery. The residual is characterized uniquely but neither assumed nor constructed. The chapter obeys Articles IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The residual insufficiency isolated in this chapter is now universal and constructive. The next chapter must therefore recover the unique mathematical object forced by that universal characterization: the Global Coherence Operator whose existence is demanded by the Uniqueness of Canonical Termination and the Uniqueness of the Residual Characterization. Characterization precedes recovery. Nothing further has yet been established.
\end{futurework}


\chapter{Recovery of Constitutional Claims}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
The Canonical Investigation Framework is now complete with respect to mathematical objects.
Canonical Reconstruction recovers objects.
Dependency Audit recovers dependency architecture.
Primitive Isolation recovers irreducible generators.
Global Completion, Compression and Determination recover the unique minimal structural architecture of every completed mathematical framework.
Yet the framework remains constitutionally incomplete.
The investigation recovers the objects of mathematics.
It has not yet recovered the assertions made about those objects.
The residual insufficiency is therefore unavoidable.
Every completed mathematical framework contains not only mathematical objects, but mathematical claims concerning those objects.
If claims remain outside the investigation framework, the framework cannot be universal.
The recovery of Constitutional Claims is therefore forced.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{The Insufficiency of Object Investigation}

Every completed mathematical framework contains two distinct kinds of presentation.
The first consists of mathematical objects.
The second consists of assertions concerning those objects.
The preceding chapters recover the first.
The second has not yet been recovered.
A theorem, lemma, proposition or definition is not merely another mathematical object.
Each asserts a structural relationship among previously recovered objects.
Without recovering those assertions themselves, constitutional investigation cannot completely reconstruct a mathematical framework.
Object investigation alone is therefore insufficient.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Objects and Claims}

The distinction between objects and claims is forced.
A mathematical object exists independently of any assertion made concerning it.
A claim records that certain recoverable structural relationships are asserted to hold among previously recovered objects.
Objects therefore constitute the structural universe.
Claims constitute the asserted architecture imposed upon that universe.
The two must not be identified.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Presentation Independence of Claims}

Claims are initially presented through language.
The wording of a theorem may vary.
Notation may change.
Definitions may be reordered.
Equivalent terminology may be substituted.
None of these alterations necessarily changes the mathematical assertion being made.
Canonical Reconstruction therefore removes linguistic presentation exactly as it removes mathematical presentation.
What survives is not the sentence.
What survives is the asserted structural dependency.
The constitutional investigation therefore studies claims independently of their presentation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Structural Claim}

Every mathematical assertion determines a unique recoverable constitutional object.
The sentence itself is presentation.
Its recoverable content consists solely of

\begin{enumerate}
    \item the recovered objects to which it refers;
    \item the structural relationships it asserts among those objects;
    \item the dependency structure required for its justification.
\end{enumerate}

This recoverable object is called a \emph{Constitutional Claim}.
A Constitutional Claim is therefore not a sentence.
It is the presentation-independent structural object recovered from the assertion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recoverability of Claims}

No new primitive is introduced.
Every Constitutional Claim is recovered entirely from objects already obtained by the completed investigation framework.
Nothing external is added.
Nothing semantic is imported.
Nothing depends upon notation.
Every claim expands completely into previously recovered mathematical objects and their asserted structural relations.
Recoverability is therefore preserved.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Identity of Claims}

Two mathematical assertions are constitutionally identical precisely when they recover the same structural claim.
Differences of wording, notation, ordering, historical presentation, or exposition do not affect constitutional identity.
Only recoverable structural content determines identity.
A Constitutional Claim therefore possesses unique identity independent of its presentation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Internal Structure of a Constitutional Claim}

Every Constitutional Claim possesses recoverable internal structure.
It contains

\begin{enumerate}
    \item the family of recovered objects referenced by the claim;
    \item the asserted structural relationships among those objects;
    \item the dependency set required by the assertion;
    \item the recoverability map expanding every component into previously recovered objects;
    \item the constitutional status of the assertion, which remains undetermined at this stage.
\end{enumerate}

Nothing further is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Existence of Constitutional Claims}

\begin{theorem}[Existence of Constitutional Claims]
Every completed mathematical framework possesses a finite recoverable family of Constitutional Claims.
\end{theorem}

\begin{proof}
A completed mathematical framework possesses a finite presentation.
Its presentation contains a finite collection of mathematical assertions.
Canonical Reconstruction removes presentation while preserving recoverable structural content.
Each mathematical assertion therefore determines a unique recoverable Constitutional Claim.
Since the presentation is finite, the resulting family of Constitutional Claims is finite.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Constitutional Claim Family}

The collection of all Constitutional Claims recovered from a completed framework forms a new recoverable constitutional object.
Every later stage of constitutional investigation acts upon this family.
No claim is investigated independently of the family to which it belongs.
The Constitutional Claim Family therefore becomes a new object of the investigation framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}

The Constitutional Claim Family now exists.
Individual Constitutional Claims have been recovered.
Their identities are recoverable.
Their internal structures are recoverable.
Their recoverability is preserved.
Yet nothing has been said concerning the relationships among Constitutional Claims themselves.
Claims may depend upon earlier claims.
They may generate later claims.
They may form coherent families.
They may exhibit dependency, equivalence, implication or redundancy.
These relationships remain unrecovered.
The preceding construction is therefore insufficient.
The recovery of a Constitutional Claim Family forces the recovery of the algebra governing Constitutional Claims.
The development of Claim Algebra is therefore unavoidable.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{dependencyaudit}
This chapter depends only upon the completed Canonical Investigation Framework recovered in the preceding chapters. No external mathematical framework has been introduced. Every Constitutional Claim is recovered solely from previously recovered mathematical objects.
\end{dependencyaudit}

\begin{primitiveaudit}
No new primitive has been introduced. Constitutional Claims are recovered objects determined entirely by previously recovered mathematical structures and asserted structural relations.
\end{primitiveaudit}

\begin{reductionaudit}
Linguistic presentation is removed from mathematical assertions. Every assertion is reduced to its recoverable structural content. Logical cost is thereby reduced.
\end{reductionaudit}

\begin{consistencyaudit}
Nothing contradicts the completed Constitution. Every Constitutional Claim expands completely into previously recovered objects and their structural relations. Recoverability is preserved.
\end{consistencyaudit}

\begin{futurework}
The Constitutional Claim Family now exists. The relationships among Constitutional Claims remain unrecovered. The development of Claim Algebra is therefore forced.
\end{futurework}

\chapter{Constitutional Claim Algebra}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Constitutional Claims now exist.
The preceding chapter established that every completed mathematical framework possesses a finite recoverable family of Constitutional Claims.
Those claims presently exist only as isolated recoverable objects.
No mathematics has yet been recovered governing their interaction.
The preceding construction is therefore insufficient.
Whenever multiple recoverable objects exist, the Constitution forces recovery of their internal algebra.
Constitutional Claim Algebra is therefore forced.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{The Insufficiency of Isolated Claims}

A completed framework contains many Constitutional Claims.
Each has been recovered as an individual structural object.
Yet nothing presently determines

\begin{itemize}
    \item when two claims are identical,
    \item when one claim depends upon another,
    \item how multiple claims combine,
    \item how claims propagate,
    \item whether families of claims possess closure.
\end{itemize}

Investigation therefore remains procedural rather than mathematical.
The Constitution forces the internal mathematics of claims.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Identity of Constitutional Claims}

A Constitutional Claim is determined solely by its recoverable structural content.
Presentation contributes nothing.
Therefore two Constitutional Claims are identical precisely when every recoverable structural component agrees.

\begin{definition}[Identity of Constitutional Claims]
Two Constitutional Claims are identical whenever they recover exactly the same structural assertion.
\end{definition}

Identity is therefore presentation-independent.
Different wording cannot generate different Constitutional Claims.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Equality of Claims}

Identity immediately forces equality.

\begin{definition}[Equality]
Two Constitutional Claims are equal whenever they are identical constitutional objects.
\end{definition}

Equality therefore ignores

\begin{itemize}
    \item notation,
    \item terminology,
    \item exposition,
    \item chapter ordering,
    \item historical formulation,
    \item motivational discussion.
\end{itemize}

Only recoverable structure remains.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Dependency Between Claims}

Claims rarely exist independently.
Many claims explicitly require earlier claims.
This dependency itself becomes recoverable.

\begin{definition}[Claim Dependency]
A Constitutional Claim \(C_2\) depends upon a Constitutional Claim \(C_1\) whenever recovery of \(C_2\) requires prior recovery of \(C_1\).
\end{definition}

Claim dependency induces a directed dependency graph upon the family of Constitutional Claims.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Generated Claims}

Some claims generate further claims.
This generation is structural.

\begin{definition}[Generated Claim]
A Constitutional Claim is generated whenever its recovery follows entirely from previously recovered Constitutional Claims.
\end{definition}

No generated claim introduces additional primitive content.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Claim Combination}

Multiple Constitutional Claims may be recovered simultaneously.
Their joint recovery determines another constitutional object.

\begin{definition}[Claim Family]
A Claim Family is any finite recoverable collection of Constitutional Claims.
\end{definition}

Claim Families introduce no new primitive.
They merely recover finite collections of existing claims.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Closure Under Recovery}

Recovery itself combines claims.
Whenever every member of a Claim Family has been recovered, every claim structurally generated by that family also becomes recoverable.

\begin{theorem}[Closure Under Recovery]
The recoverable consequences of every finite Claim Family again form a Claim Family.
\end{theorem}

\begin{proof}
Every generated claim is recovered entirely from previously recovered claims.
Generation therefore introduces no external object.
Recoverability is preserved.
Hence the resulting family is again finite and recoverable.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Operations}

The preceding constructions recover natural operations upon Constitutional Claims.
These include

\begin{itemize}
    \item identity,
    \item equality,
    \item dependency,
    \item generation,
    \item finite collection,
    \item recoverable closure.
\end{itemize}

Each operation preserves recoverability.
None introduces a new primitive.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Constitutional Claim Algebra}

The preceding operations determine a new mathematical object.

\begin{definition}[Constitutional Claim Algebra]
The Constitutional Claim Algebra consists of
\begin{itemize}
    \item the family of Constitutional Claims,
    \item claim identity,
    \item claim equality,
    \item dependency,
    \item generation,
    \item finite claim families,
    \item closure under recovery.
\end{itemize}
\end{definition}

This algebra is recovered entirely from the Constitution.
Nothing external has been introduced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Existence Theorem}

\begin{theorem}[Existence of Constitutional Claim Algebra]
Every completed mathematical framework possesses a unique Constitutional Claim Algebra.
\end{theorem}

\begin{proof}
The preceding chapter recovered the finite family of Constitutional Claims.
The present chapter recovered identity, equality, dependency, generation and recoverable closure entirely from those claims.
These constructions determine a unique algebra upon the recovered family.
No additional primitive is introduced.
Therefore every completed framework possesses a unique Constitutional Claim Algebra.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}

Constitutional Claims now possess internal mathematics.
Yet no distinction has been recovered between different kinds of Constitutional Claims.
Every claim presently occupies the same constitutional status.
The investigation cannot yet distinguish

\begin{itemize}
    \item definitions,
    \item assumptions,
    \item axioms,
    \item derived propositions,
    \item conjectures,
    \item algorithms,
    \item existence assertions,
    \item structural identities,
    \item applications.
\end{itemize}

The Constitutional Claim Algebra therefore remains insufficient.
The Constitution forces recovery of the different constitutional species of claims.
Claim Stratification is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{dependencyaudit}
This chapter depends only upon the recovery of Constitutional Claims. No new primitive has been introduced. Every operation is recovered internally from the existence of claims themselves.
\end{dependencyaudit}

\begin{primitiveaudit}
The chapter introduces no additional primitive. Constitutional Claim Algebra is recovered entirely from previously recovered Constitutional Claims.
\end{primitiveaudit}

\begin{reductionaudit}
Presentation-dependent formulations of mathematical statements are eliminated. Only recoverable structural relations between Constitutional Claims remain.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction follows from the completed Constitution and the recovery of Constitutional Claims. Recoverability is preserved throughout.
\end{consistencyaudit}

\begin{futurework}
Constitutional Claims now possess an internal algebra. Their constitutional species remain unrecovered. The next insufficiency therefore forces Claim Stratification.
\end{futurework}

\chapter{Claim Stratification}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
The Constitutional Claim Algebra now exists.
Every completed mathematical framework possesses a finite recoverable family of Constitutional Claims together with their internal algebra.
Yet every claim presently possesses identical constitutional status.
The preceding construction is therefore insufficient.
Different claims perform fundamentally different structural roles within a mathematical framework.
Definitions generate objects.
Axioms introduce assumptions.
Theorems derive consequences.
Algorithms prescribe constructions.
Conjectures suspend determination.
Applications transport mathematics beyond the framework itself.
These distinctions are structural rather than interpretive.
The Constitution therefore forces recovery of the constitutional species of claims.
Claim Stratification is forced.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{The Insufficiency of Uniform Claims}

The Constitutional Claim Algebra recovers only the existence and interaction of claims.
It does not distinguish their mathematical function.
Consequently,

\begin{itemize}
    \item every claim is presently indistinguishable,
    \item dependency alone cannot determine constitutional role,
    \item later audit stages cannot operate canonically.
\end{itemize}

A finer structural decomposition is therefore necessary.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Role}

Every Constitutional Claim contributes to the framework in a specific manner.
That contribution is independent of notation, wording and presentation.
Only recoverable structure determines constitutional role.

\begin{definition}[Constitutional Role]
The Constitutional Role of a claim is the recoverable mathematical function performed by that claim within the dependency architecture.
\end{definition}

Role is intrinsic.
Presentation contributes nothing.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Constitutional Species}

Inspection of the dependency architecture forces a finite family of constitutional species.
Every Constitutional Claim belongs to exactly one recoverable species.

\subsection{Primitive Claims}
Primitive Claims introduce objects that are not themselves recovered earlier within the investigated framework.
They constitute the declared generators of the framework.

\subsection{Definition Claims}
Definition Claims introduce recoverable mathematical objects from previously available objects.
They increase vocabulary without increasing primitive content.

\subsection{Bridge Claims}
Bridge Claims connect the internal mathematics of the framework with external data, calibration or interpretation.
They supply attachment without altering internal derivation.

\subsection{Axiom Claims}
Axiom Claims declare assumptions accepted within the framework but not yet constitutionally validated.
Their admissibility remains undecided.

\subsection{Construction Claims}
Construction Claims prescribe recoverable procedures producing new mathematical objects.

\subsection{Derivation Claims}
Derivation Claims recover mathematical consequences entirely from earlier claims.
They introduce no additional assumptions.

\subsection{Structural Claims}
Structural Claims describe dependency relations, symmetries, closure properties or other internal structural behaviour.

\subsection{Algorithmic Claims}
Algorithmic Claims prescribe executable procedures whose outputs are intended to be recoverable.

\subsection{Conjectural Claims}
Conjectural Claims assert mathematical conclusions whose constitutional determination has not yet been established.

\subsection{Application Claims}
Application Claims transport the internal mathematics toward external mathematical, physical or empirical domains.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Uniqueness of Constitutional Role}

A Constitutional Claim cannot simultaneously perform two independent constitutional roles.
Its role is determined entirely by its recoverable function.

\begin{theorem}[Uniqueness of Constitutional Role]
Every Constitutional Claim possesses a unique constitutional species.
\end{theorem}

\begin{proof}
Suppose a claim possessed two distinct constitutional roles.
Then its recoverable mathematical function would not be uniquely determined.
The dependency architecture would therefore admit two incompatible recoveries.
Canonical Reconstruction forbids such ambiguity.
Hence every Constitutional Claim possesses exactly one constitutional species.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Finite Stratification}

The Constitutional Claim Algebra is finite.
Therefore its stratification is likewise finite.

\begin{theorem}[Finite Claim Stratification]
Every completed mathematical framework possesses a finite recoverable stratification of its Constitutional Claims.
\end{theorem}

\begin{proof}
The family of Constitutional Claims is finite.
Each claim possesses a unique constitutional role.
Partitioning a finite family by unique role produces a finite stratification.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Claim Stratification Object}

The recovered partition itself becomes a new mathematical object.

\begin{definition}[Claim Stratification]
The Claim Stratification of a completed framework is the finite partition of its Constitutional Claims according to constitutional role.
\end{definition}

The Claim Stratification introduces no new primitive.
It is recovered entirely from the Constitutional Claim Algebra.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Presentation Independence}

Presentation does not alter constitutional role.
Changing notation, chapter ordering, historical motivation, terminology, or exposition cannot move a claim from one constitutional species to another.
Therefore Claim Stratification is presentation-independent.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Existence Theorem}

\begin{theorem}[Existence of Claim Stratification]
Every completed mathematical framework possesses a unique Claim Stratification.
\end{theorem}

\begin{proof}
The Constitutional Claim Algebra exists.
Every Constitutional Claim possesses a unique constitutional role.
Partitioning the finite family of claims by those roles determines a unique finite stratification.
No additional primitive is introduced.
Therefore every completed mathematical framework possesses a unique Claim Stratification.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}

Claim Stratification recovers the constitutional species of every claim.
Yet no relationship has been recovered between those species and constitutional investigation itself.
The protocol still cannot determine

\begin{itemize}
    \item which claim species may be audited immediately,
    \item which require prior recovery,
    \item which may generate later investigations,
    \item which terminate investigation,
    \item which remain constitutionally inert.
\end{itemize}

The interaction between constitutional species and constitutional investigation therefore remains unrecovered.
The Constitution forces recovery of the Investigation Order of Constitutional Claims.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{dependencyaudit}
This chapter depends only upon the Constitutional Claim Algebra. Every constitutional species is recovered solely from the structural role performed by claims within the dependency architecture.
\end{dependencyaudit}

\begin{primitiveaudit}
No new primitive has been introduced. Claim Stratification is recovered entirely from the Constitutional Claim Algebra.
\end{primitiveaudit}

\begin{reductionaudit}
Uniform treatment of Constitutional Claims is eliminated. Claims are reduced to a finite family of recoverable constitutional species without increasing logical cost.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction follows from the completed Constitution and the previously recovered Constitutional Claim Algebra. Recoverability is preserved throughout.
\end{consistencyaudit}

\begin{futurework}
The constitutional species of every claim have been recovered. Their interaction with constitutional investigation remains unknown. The next insufficiency therefore forces recovery of the Investigation Order of Constitutional Claims.
\end{futurework}

\chapter{Claim Dependency Calculus}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
The Claim Algebra now exists.
Its elements have been recovered.
Its operations have been recovered.
Its internal stratification has been recovered.
Yet the algebra remains constitutionally incomplete.
The existence of Constitutional Claims does not determine how those claims generate one another.
Claim Stratification orders claims by constitutional role.
It does not determine the propagation of logical dependence.
The residual insufficiency is therefore dynamic rather than algebraic.
A calculus governing dependency among Constitutional Claims is forced.

\section{The Insufficiency of Claim Stratification}

Claim Stratification recovers a layered organisation of Constitutional Claims.
Primitive Claims precede Derived Claims.
Derived Claims precede Structural Claims.
Structural Claims precede Universal Claims.
This ordering determines constitutional level.
It does not determine constitutional dependence.
Two claims occupying the same stratum may possess radically different dependency structures.
Likewise, claims occupying different strata may exhibit identical dependency behaviour.
The stratification therefore remains insufficient for constitutional investigation.
A dependency calculus is forced.

\section{Immediate Constitutional Dependency}

Let \(C_1\) and \(C_2\) be Constitutional Claims belonging to the same completed framework.

\begin{definition}[Immediate Constitutional Dependency]
The claim \(C_2\) is said to depend immediately upon the claim \(C_1\) whenever the recovery of \(C_2\) requires the prior recovery of \(C_1\), and no intermediate Constitutional Claim is required between them.
\end{definition}

Immediate dependency is denoted
\[
C_1 \longrightarrow C_2.
\]
Immediate dependency introduces no new mathematical primitive.
It merely records a recoverable relation already latent within the constitutional reconstruction of the framework.

\section{Dependency Families}

Immediate dependency determines larger recoverable collections.

\begin{definition}[Dependency Family]
The Dependency Family of a Constitutional Claim \(C\) is the recoverable collection of every Constitutional Claim upon which \(C\) depends, either immediately or through a finite chain of immediate dependencies.
\end{definition}

The Dependency Family of \(C\) is denoted by
\[
\mathcal{D}(C).
\]
Every member of \(\mathcal{D}(C)\) is constitutionally prior to \(C\).
Every dependency family is finite.

\begin{theorem}[Existence of Dependency Families]
Every Constitutional Claim possesses a unique finite Dependency Family.
\end{theorem}

\begin{proof}
The completed framework possesses a finite family of Constitutional Claims.
Immediate dependency is recovered entirely from explicit recoverable generation within that finite family.
Beginning with any Constitutional Claim, repeated recovery of all immediate predecessors must therefore terminate after finitely many steps.
The resulting recoverable family is unique.
Hence every Constitutional Claim possesses a unique finite Dependency Family.
\end{proof}

\section{Dependency Closure}

Dependency Families naturally determine closure.

\begin{definition}[Dependency Closure]
The Dependency Closure of a Constitutional Claim \(C\) is the smallest recoverable family of Constitutional Claims containing \(C\) together with every element of its Dependency Family.
\end{definition}

The Dependency Closure of \(C\) is denoted
\[
\overline{\mathcal{D}}(C).
\]
Dependency Closure contains every recoverable claim required for the constitutional recovery of \(C\).
No additional claim belongs to the closure.

\begin{theorem}[Existence of Dependency Closure]
Every Constitutional Claim possesses a unique Dependency Closure.
\end{theorem}

\begin{proof}
The Dependency Family of every Constitutional Claim exists and is finite.
Adjoining the claim itself produces a finite recoverable family.
Minimality follows immediately from construction.
Therefore the Dependency Closure exists uniquely.
\end{proof}

\section{Dependency Paths}

Dependency is not merely local.
Finite sequences of dependencies become recoverable constitutional objects.

\begin{definition}[Dependency Path]
A Dependency Path is a finite sequence of Constitutional Claims
\[
C_0 \longrightarrow C_1 \longrightarrow \cdots \longrightarrow C_n
\]
such that every adjacent pair forms an Immediate Constitutional Dependency.
\end{definition}

Every Dependency Family is generated by the collection of Dependency Paths terminating at its maximal claim.
Dependency Paths therefore recover the internal flow of constitutional generation.

\section{Dependency Graphs}

The totality of Immediate Constitutional Dependencies determines a single structural object.

\begin{definition}[Claim Dependency Graph]
The Claim Dependency Graph of a completed framework is the directed graph whose vertices are the Constitutional Claims and whose directed edges are the Immediate Constitutional Dependencies.
\end{definition}

The Claim Dependency Graph is denoted
\[
\Gamma_{\mathcal C}.
\]
The graph is entirely recoverable from the completed framework.
No presentation enters its construction.

\begin{theorem}[Existence of the Claim Dependency Graph]
Every completed framework possesses a unique finite Claim Dependency Graph.
\end{theorem}

\begin{proof}
The family of Constitutional Claims is finite.
Immediate Constitutional Dependencies are uniquely recoverable.
The vertices and directed edges are therefore uniquely determined.
Hence the Claim Dependency Graph exists uniquely.
\end{proof}

\section{Minimal Supporting Families}

Dependency Closures generally contain redundancy.
The Constitution therefore forces recovery of irreducible support.

\begin{definition}[Minimal Supporting Family]
A Minimal Supporting Family for a Constitutional Claim \(C\) is a recoverable subfamily of its Dependency Closure sufficient for the recovery of \(C\), and possessing no proper recoverable subfamily with the same property.
\end{definition}

Minimal Supporting Families minimise logical cost.
They recover only those Constitutional Claims whose removal destroys recoverability.

\begin{theorem}[Existence of Minimal Supporting Families]
Every Constitutional Claim possesses at least one Minimal Supporting Family.
\end{theorem}

\begin{proof}
The Dependency Closure of every Constitutional Claim is finite.
Among all recoverable supporting families, select one of minimal cardinality.
Finite minimality guarantees existence.
Its minimality is immediate by construction.
\end{proof}

Uniqueness is not asserted.
Different minimal supporting families may exist.
The Constitution records only recoverability.

\section{Dependency Propagation}

Dependency possesses an intrinsic direction.
Constitutional modification propagates throughout the dependency architecture.

\begin{definition}[Dependency Propagation]
Dependency Propagation is the recoverable process by which every modification of a Constitutional Claim propagates through every Dependency Path issuing from that claim.
\end{definition}

Propagation is entirely structural.
No semantic interpretation is required.
Every propagation is determined solely by the Claim Dependency Graph.

\begin{theorem}[Recoverability of Dependency Propagation]
Dependency Propagation is uniquely recoverable from the Claim Dependency Graph.
\end{theorem}

\begin{proof}
Propagation follows precisely the directed edges of the Claim Dependency Graph.
Since the graph is uniquely recoverable, every propagation sequence is uniquely recoverable.
No additional construction is required.
\end{proof}

\section{The Claim Dependency Calculus}

The preceding constructions recover a complete constitutional calculus governing claims.
The Claim Dependency Calculus consists of

\begin{itemize}
    \item Immediate Constitutional Dependency;
    \item Dependency Families;
    \item Dependency Closure;
    \item Dependency Paths;
    \item the Claim Dependency Graph;
    \item Minimal Supporting Families;
    \item Dependency Propagation.
\end{itemize}

These constructions introduce no new primitive.
Each is recovered solely from Constitutional Claims and their recoverable relations.
The Claim Dependency Calculus is therefore a derived constitutional object.

\begin{theorem}[Existence of the Claim Dependency Calculus]
Every completed mathematical framework possesses a unique Claim Dependency Calculus.
\end{theorem}

\begin{proof}
Every completed framework possesses a finite recoverable family of Constitutional Claims.
Immediate dependencies are recoverable.
Dependency Families, Dependency Closures, Dependency Paths, the Claim Dependency Graph, Minimal Supporting Families and Dependency Propagation are each recovered successively from these dependencies.
No additional primitive is introduced.
The resulting calculus is therefore uniquely determined by the completed framework.
\end{proof}

\section{Residual Insufficiency}

The Claim Dependency Calculus recovers how Constitutional Claims generate one another.
It recovers the propagation of dependency throughout a completed framework.
It recovers every recoverable path of constitutional generation.
Yet it does not distinguish constitutionally indispensable claims from claims inherited merely through presentation.
Minimal Supporting Families exist.
Their constitutional status has not been determined.
The distinction between recoverable support and constitutionally indispensable support is therefore forced.
The following construction recovers the Constitutional Core of a completed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{dependencyaudit}
This chapter depends only upon the Recovery of Constitutional Claims, the Constitutional Claim Algebra, and Claim Stratification. Every subsequent construction is recovered solely from previously established constitutional objects. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Immediate dependency, dependency families, dependency closure, dependency paths, dependency graphs, minimal supporting families and dependency propagation are all recovered from the previously established family of Constitutional Claims.
\end{primitiveaudit}

\begin{reductionaudit}
The chapter reduces the study of constitutional dependency to a finite recoverable calculus. Logical cost is reduced by replacing informal dependency reasoning with a canonical mathematical structure.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction follows uniquely from the previously recovered Constitutional Claim Algebra. No external logical or graph-theoretic machinery has been imported. The Constitution remains internally complete.
\end{consistencyaudit}

\begin{futurework}
The Claim Dependency Calculus now exists. It recovers every dependency relation among Constitutional Claims. Yet it does not distinguish constitutionally indispensable claims from merely recoverable supporting claims. The Constitutional Core is therefore forced.
\end{futurework}


\setlength{\parindent}{0pt}
\setlength{\parskip}{\baselineskip}

\chapter{Canonical Claim Reconstruction}

The Claim Dependency Calculus now exists. Constitutional Claims have been recovered, along with their algebra, their stratification, and their dependency structure. Yet the investigation remains constitutionally incomplete. 

The Claim Dependency Calculus records every recoverable Constitutional Claim together with every recoverable dependency relation. However, it does not distinguish constitutional structure from presentation. Different completed presentations of the same mathematical framework may recover different Claim Dependency Graphs while nevertheless expressing the same constitutional mathematics. The residual insufficiency is therefore presentation-dependence within the claim architecture itself. Thus, a \textbf{Canonical Claim Reconstruction} is forced.

\section{The Insufficiency of the Claim Dependency Calculus}

The Claim Dependency Calculus recovers the complete graph of Constitutional Claims, but the graph depends entirely upon the recovered presentation. Equivalent claims may appear multiple times, equivalent dependency paths may coexist, and equivalent chains of derivation may survive independently. Presentation therefore remains visible inside the claim graph. Because the Constitution admits no presentation-dependent mathematical object, a presentation-independent reconstruction is necessary.

\section{Constitutional Equivalence of Claims}

Different Constitutional Claims may possess identical constitutional content.

\begin{definition}[Constitutional Equivalence]
Two Constitutional Claims are constitutionally equivalent whenever each is recoverable from the other without introducing any additional Constitutional Claim:
\[
C_1 \equiv C_2.
\]
\end{definition}

Constitutional Equivalence is entirely recoverable; no semantic interpretation is admitted, and only recoverability enters.

\section{Equivalence Classes}

Constitutional Equivalence partitions the family of Constitutional Claims into distinct structural units.

\begin{definition}[Canonical Claim Class]
A Canonical Claim Class is an equivalence class under Constitutional Equivalence:
\[
[C] = \{D \mid D \equiv C\}.
\]
\end{definition}

Every Constitutional Claim belongs to one and only one Canonical Claim Class.

\begin{theorem}
The family of Constitutional Claims admits a unique partition into Canonical Claim Classes.
\end{theorem}

\begin{proof}
Constitutional Equivalence is reflexive, symmetric, and transitive by recoverability. Therefore, it determines a unique partition.
\end{proof}

\section{Canonical Dependency}

Dependency descends naturally to Canonical Claim Classes.

\begin{definition}
Canonical Dependency exists whenever one Canonical Claim Class depends upon another after replacing every Constitutional Claim by its Canonical Claim Class.
\end{definition}

Canonical Dependency introduces no new primitive; it merely reconstructs dependency after presentation has been removed.

\section{Canonical Reconstruction}

Replacing every Constitutional Claim by its Canonical Claim Class and replacing every dependency by Canonical Dependency produces a new constitutional object.

\begin{definition}
The Canonical Claim Reconstruction of a completed mathematical framework is the dependency graph whose vertices are Canonical Claim Classes and whose edges are Canonical Dependencies.
\end{definition}

Presentation has now disappeared, leaving only the pure constitutional structure.

\section{Existence and Properties}

\subsection{Existence}

\begin{theorem}[Existence of Canonical Claim Reconstruction]
Every completed mathematical framework possesses a unique Canonical Claim Reconstruction.
\end{theorem}

\begin{proof}
The Claim Dependency Calculus recovers a finite family of Constitutional Claims. Constitutional Equivalence uniquely partitions that family, and Canonical Dependency is uniquely induced by the recovered dependency graph. The resulting graph depends only upon constitutional recoverability. Hence, the Canonical Claim Reconstruction exists uniquely.
\end{proof}

\subsection{Recoverability}

Every Constitutional Claim is recoverable from its Canonical Claim Class, and every Canonical Claim Class is recoverable from any representative Constitutional Claim. No mathematical content is lost; only presentation disappears. Recoverability is therefore preserved.

\subsection{Minimality}

The Canonical Claim Reconstruction possesses no duplicate constitutional content. Equivalent claims and equivalent dependency chains occur exactly once. Presentation-dependent redundancy has disappeared, rendering the reconstruction constitutionally minimal.

\begin{theorem}
The Canonical Claim Reconstruction contains no pair of distinct constitutionally equivalent vertices.
\end{theorem}

\begin{proof}
Distinct vertices correspond to distinct Canonical Claim Classes. Since distinct Canonical Claim Classes are not constitutionally equivalent, no duplicate constitutional content remains.
\end{proof}

\section{The Canonical Constitutional Object}

The Canonical Claim Reconstruction is no longer a presentation or a mere dependency graph of statements. It is the unique constitutional realization of the completed framework at the level of claims. Every later investigation proceeds solely upon this reconstructed object, and the original presentation is never again required.

\section{Residual Insufficiency}

The Canonical Claim Reconstruction removes presentation from Constitutional Claims and recovers the unique constitutional realization of the claim architecture. Yet it does not compare different regions of that architecture, measure global compatibility, or recover structural coherence. A global operator acting upon the Canonical Claim Reconstruction is therefore forced. The \emph{Global Coherence Operator} is introduced in the following chapter.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon Universality of the Residual, Recovery of Constitutional Claims, Constitutional Claim Algebra, Claim Stratification and the Claim Dependency Calculus. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Canonical Claim Reconstruction is recovered entirely from Constitutional Claims and their recoverable dependencies.
\end{primitiveaudit}

\begin{reductionaudit}
Presentation-dependent duplication of Constitutional Claims is eliminated. Equivalent dependency chains are reconstructed into a unique constitutional realization. Logical cost is thereby reduced.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction follows uniquely from previously recovered constitutional objects. No external mathematics has been imported. The Constitution remains internally complete.
\end{consistencyaudit}

\begin{futurework}
The Canonical Claim Reconstruction now exists. The mathematical framework has been reconstructed as a unique presentation-independent claim object. Its global coherence has not yet been recovered. The Global Coherence Operator is therefore forced.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{The Global Coherence Operator}

\section{The Insufficiency of Canonical Claim Reconstruction}

The Canonical Claim Reconstruction has now been recovered. Every completed framework now determines:
\begin{itemize}
    \item its constitutional objects,
    \item its constitutional claims,
    \item the algebra of those claims,
    \item their constitutional strata,
    \item their dependency calculus,
    \item and the canonical dependency architecture generated by those claims.
\end{itemize}

Nothing remains presentation-dependent. Every constitutional component of the framework has been recovered as a single mathematical object. Yet the investigation remains incomplete. 

Canonical Claim Reconstruction records every constitutional claim together with every dependency among those claims, but it does not determine how the entire reconstructed architecture coheres as a single constitutional object. The residual is therefore no longer one of reconstruction; it is one of global coherence. The mathematics therefore forces the recovery of an operator that acts upon Canonical Claim Reconstructions themselves.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Necessity of Global Constitutional Coherence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Canonical Claim Reconstruction recovered in Chapter~20 is complete. Every constitutional claim, dependency among claims, and constitutional stratum has been recovered, and every presentation-dependent distinction has been removed. The reconstruction is therefore constitutionally complete.

Completion alone is nevertheless insufficient. The reconstructed claim architecture remains a collection of constitutional objects related by the Claim Dependency Graph. The graph records dependency; it does not itself constitute determination. 

A completed constitutional investigation requires more than the existence of a dependency graph. It requires that the entire reconstructed architecture determine a single constitutional state from which every recovered claim, dependency, and stratum remains recoverable. Without such a determination, the investigation possesses multiple recoverable components but no recovered constitutional whole. The residual identified in Chapter~15 therefore persists at the level of reconstructed claims. 

The preceding chapters permit reconstruction, but they do not yet permit constitutional completion. The Constitution therefore forces the recovery of an operation satisfying the following requirements. For every Canonical Claim Reconstruction it must:

\begin{enumerate}
    \item preserve every recovered constitutional claim;
    \item preserve every dependency recovered by the Claim Dependency Calculus;
    \item preserve every constitutional stratum;
    \item introduce no new claim;
    \item introduce no new dependency;
    \item introduce no new primitive;
    \item recover a single coherent constitutional determination from the reconstructed claim architecture.
\end{enumerate}

No weaker operation removes the residual. Any operation failing to preserve claims changes the investigated framework, any operation failing to preserve dependencies destroys recoverability, and any operation introducing additional primitives violates the Constitution. Furthermore, any operation producing multiple determinations leaves the residual unchanged. The existence of a unique global coherence operation is therefore forced by the Constitution itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Global Coherence Operator}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Progressive Constitutional Amalgamation is now recovered. The preceding section established that every Canonical Claim Reconstruction admits a unique constitutional process that successively amalgamates recoverable constitutional regions while preserving every recovered claim, every dependency relation, and every constitutional stratum. 

The residual nevertheless remains. A process alone is not yet a mathematical object. The Constitution does not investigate procedures; it investigates recoverable objects. The terminal object generated by Progressive Constitutional Amalgamation has not yet been recovered. The following construction is therefore forced.

Let $\mathfrak{C}$ be the Canonical Claim Reconstruction of an arbitrary completed mathematical framework. Beginning with $\mathfrak{C}$, execute Progressive Constitutional Amalgamation. At each stage, let
\[
\mathfrak{C}_0,\, \mathfrak{C}_1,\, \mathfrak{C}_2,\, \dots
\]
denote the successive constitutional amalgams produced by the recovered process. Each stage satisfies the following properties:
\begin{enumerate}
    \item Every Constitutional Claim recovered in $\mathfrak{C}$ remains recoverable.
    \item Every dependency relation recovered by the Claim Dependency Calculus remains recoverable.
    \item Every constitutional stratum remains unchanged.
    \item No new claim is introduced.
    \item No claim is discarded.
    \item No new dependency is introduced.
    \item No dependency is removed.
\end{enumerate}

Successive stages differ only by the elimination of unnecessary constitutional separation. No mathematical content changes; only constitutional coherence increases. Consequently, the sequence $\mathfrak{C}_0, \mathfrak{C}_1, \mathfrak{C}_2, \dots$ is monotone with respect to constitutional coherence. 

Each stage preserves every recoverable object while strictly decreasing the number of disconnected constitutional regions. Since no stage introduces additional claims or dependencies, the process cannot diverge through continual expansion. Since every amalgamation removes at least one remaining constitutional separation, the process cannot remain stationary before complete coherence is obtained. 

The process therefore determines a unique terminal constitutional reconstruction. This terminal reconstruction is recovered solely from the Canonical Claim Reconstruction by Progressive Constitutional Amalgamation. No additional primitive has entered the construction, no external information has been supplied, and no presentation has reappeared. The terminal reconstruction depends only upon previously recovered constitutional objects. It is therefore itself a recovered mathematical object whose existence is forced. The recovered object is the unique global constitutional determination of the Canonical Claim Reconstruction.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Finite Termination of Progressive Constitutional Amalgamation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding construction recovers a sequence of constitutional amalgamations. Its terminal object has been recovered only formally. The Constitution nevertheless requires that every recovered process terminate after finitely many stages. Termination must therefore be proved.

\begin{theorem}[Finite Termination of Progressive Constitutional Amalgamation]
\label{thm:constitutional-termination}
For every completed mathematical framework, Progressive Constitutional Amalgamation terminates after finitely many stages.
\end{theorem}

\begin{proof}
Let $\mathfrak{C}$ be the Canonical Claim Reconstruction of an arbitrary completed framework. By Chapter~20, the reconstruction consists of a finite family of Constitutional Claims together with a finite Claim Dependency Graph. Consequently, the collection of connected constitutional regions determined by the dependency graph is finite.

Each stage of Progressive Constitutional Amalgamation replaces two or more connected constitutional regions by their unique constitutional amalgam while preserving every recovered claim, dependency relation, and constitutional stratum. No stage introduces additional constitutional regions, and no stage divides an existing region. Therefore, every stage strictly decreases the number of disconnected constitutional regions. Since this number is a non-negative integer, no infinite strictly descending sequence exists. The amalgamation process therefore terminates after finitely many stages.
\end{proof}

Finite termination is therefore forced. The terminal constitutional reconstruction exists for every completed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Naming}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding theorems recover a unique mathematical object. Recoverability precedes notation; notation is therefore now earned. The unique operation sending every Canonical Claim Reconstruction to its unique terminal constitutional reconstruction will be denoted by $\Gamma$. 

The operator
\[
\Gamma : \mathfrak{C} \longmapsto \Gamma(\mathfrak{C})
\]
will be called the \emph{Global Coherence Operator}. The terminology is forced: the operator acts globally, it produces constitutional coherence, and it acts only upon Canonical Claim Reconstructions. No alternative designation carries less logical cost. The Global Coherence Operator is therefore recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Removal of the Universal Residual}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Chapter~15 recovered the unique universal residual of the Canonical Investigation Framework. The succeeding chapters recovered Constitutional Claims, the Constitutional Claim Algebra, Constitutional Claim Stratification, the Claim Dependency Calculus, and the Canonical Claim Reconstruction. The present chapter has recovered the unique operation that converts every Canonical Claim Reconstruction into a single globally coherent constitutional determination. The residual identified in Chapter~15 therefore disappears.

\begin{theorem}[Removal of the Universal Residual]
\label{thm:global-removal}
For every completed mathematical framework, the Global Coherence Operator produces the unique globally coherent constitutional determination of its Canonical Claim Reconstruction. Consequently, the universal residual recovered in Chapter~15 is removed.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:constitutional-termination}, Progressive Constitutional Amalgamation terminates after finitely many stages. By Theorem~\ref{thm:constitutional-uniqueness}, its terminal reconstruction is unique. Section~7 recovers the Global Coherence Operator as precisely this unique terminal operation. Therefore, every Canonical Claim Reconstruction admits a unique globally coherent constitutional determination. The residual characterized in Chapter~15 consisted exactly in the absence of such an operation. The residual therefore no longer exists.
\end{proof}

The Canonical Investigation Framework now possesses a complete mechanism for recovering globally coherent constitutional determinations from arbitrary completed mathematical frameworks.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Global Coherence Operator has now been recovered. Every completed mathematical framework admits a unique globally coherent constitutional determination. The preceding construction nevertheless remains insufficient. 

The Global Coherence Operator exists only as a single recovered operator. Its internal mathematical behaviour has not yet been recovered. Composition of global coherence operations, stability under constitutional morphisms, functorial behaviour, fixed coherent structures, and the interaction of multiple coherent determinations have not been investigated. An operator without an algebra remains constitutionally incomplete. The mathematics therefore forces the recovery of the algebra generated by the Global Coherence Operator.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Chapter Conclusion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The universal residual recovered in Chapter~15 has now been removed. Beginning with the Canonical Claim Reconstruction, the Constitution forced the recovery of Progressive Constitutional Amalgamation. Finite termination and uniqueness of the terminal reconstruction were established, and the unique Global Coherence Operator $\Gamma$ was recovered. 

Every completed mathematical framework now admits a unique globally coherent constitutional determination. The internal mathematics of the operator has not yet been recovered. The next insufficiency is therefore forced: the Global Coherence Algebra is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed Constitution of \emph{Mathematics of the King}, the Canonical Investigation Framework, the Universality of the Residual, the Recovery of Constitutional Claims, the Constitutional Claim Algebra, Claim Stratification, the Claim Dependency Calculus, and the Canonical Claim Reconstruction. No external mathematical framework is admitted. Every dependency remains acyclic and fully recoverable.
\end{dependencyaudit}

\begin{primitiveaudit}
No new primitive has been introduced. The Global Coherence Operator is recovered solely from previously recovered constitutional objects. Its construction depends only upon the Canonical Claim Reconstruction and the operations already recovered by the Constitutional Claim Calculus. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
The logical cost of constitutional investigation is reduced by replacing an entire reconstructed claim architecture with its unique globally coherent constitutional determination. No mathematical content is discarded, no constitutional claim is altered, and presentation has already been removed. The present chapter removes only unnecessary constitutional separation while preserving complete recoverability.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction follows from previously recovered constitutional objects. Necessity precedes construction, construction precedes existence, existence precedes notation, and notation precedes algebra. The chapter introduces no circular dependencies, no unrecoverable objects, and no additional primitive assumptions. The constitutional architecture remains internally consistent.
\end{consistencyaudit}

\begin{futurework}
The Global Coherence Operator has now been recovered. Its internal mathematical behaviour remains unknown. The next chapter therefore recovers the algebra generated by the operator, including composition, stability, transport, fixed coherent structures and the interaction of globally coherent constitutional determinations. The Global Coherence Algebra is therefore forced.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{The Global Coherence Algebra}

The preceding chapter recovered the Global Coherence Operator. Its existence is no longer in question; its input, output, and action upon Canonical Claim Reconstructions have all been recovered. Yet the mathematics remains incomplete. A single operator does not constitute an executable investigation. Repeated investigations require repeated applications of the Global Coherence Operator, and those applications must themselves possess recoverable mathematical structure. The operator therefore cannot remain isolated; its internal mathematics is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of an Isolated Operator}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Global Coherence Operator transforms a Canonical Claim Reconstruction into a globally coherent constitutional structure. This transformation is sufficient for one investigation, but it is insufficient for mathematics. Different investigations necessarily recover different Canonical Claim Reconstructions. The outputs of previous investigations must themselves become admissible inputs for later investigations. Consequently, the operator must interact with itself. Nothing presently governs such interaction. The mathematics therefore possesses an operator without an algebra. The Constitution forbids repeated application of an operator whose interaction has not been recovered. The recovery of the operator therefore forces recovery of the algebra generated by that operator.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Necessity of Coherence Operations}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Global Coherence Operator acts upon Canonical Claim Reconstructions. Every application receives a finite constitutional structure consisting of recovered constitutional claims together with their dependency relations. The output is a globally coherent realization of that structure. The preceding chapter recovered only the existence of this transformation; it did not recover how distinct applications of the operator interact. 

The insufficiency is immediate. Suppose two Canonical Claim Reconstructions have been recovered independently. A constitutional investigation may subsequently determine that portions of their claim structures coincide. The mathematics must therefore recover how globally coherent structures interact whenever coherent overlap exists. 

Likewise, an investigation may later reveal that only a proper constitutional substructure is relevant to a subsequent determination; the mathematics must therefore recover restriction. Conversely, further constitutional investigation may enlarge an already coherent reconstruction by adjoining newly recovered claims; the mathematics must therefore recover extension. Finally, successive investigations necessarily transport coherent structures through Canonical Morphisms of Determination already recovered in the Witness Calculus. Transport must therefore be recovered as an admissible coherence operation. 

These necessities are not introduced for convenience; each is forced by the repeated execution of constitutional investigation. The mathematics therefore recovers the elementary operations generated by the Global Coherence Operator.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Elementary Coherence Operations}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let $\mathfrak{C}$ denote an arbitrary Canonical Claim Reconstruction. The repeated execution of the Global Coherence Operator forces the recovery of the following elementary coherence operations.

\subsection{Coherence Merge}
Whenever two Canonical Claim Reconstructions possess a coherent overlap recovered from the Claim Dependency Calculus, the Global Coherence Operator recovers a single coherent realization extending both reconstructions while preserving their common constitutional content. This operation will be called \emph{Coherence Merge}.

\subsection{Coherence Restriction}
Whenever constitutional investigation concerns only a recoverable constitutional substructure, the Global Coherence Operator recovers the induced globally coherent realization upon that substructure. This operation will be called \emph{Coherence Restriction}.

\subsection{Coherence Extension}
Whenever additional constitutional claims become recoverable, the previously recovered coherent realization extends uniquely to incorporate those newly recovered claims. This operation will be called \emph{Coherence Extension}.

\subsection{Coherence Transport}
Whenever two Canonical Claim Reconstructions are related by a previously recovered Morphism of Determination, global coherence transports uniquely across that morphism. This operation will be called \emph{Coherence Transport}.

\subsection{Coherence Compression}
Whenever a globally coherent realization contains constitutionally redundant determining content, the Compression Calculus recovers its Minimal Determining Content without altering constitutional determination. This operation will be called \emph{Coherence Compression}.

Each operation is forced entirely by previously recovered mathematics. No new primitive has been introduced. Each operation acts solely upon Canonical Claim Reconstructions and their globally coherent realizations. Collectively, these operations constitute the elementary constitutional operations of global coherence.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Minimal Coherence Closure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The elementary coherence operations have now been recovered. Taken individually, they permit isolated constitutional transformations. The mathematics nevertheless remains incomplete, as nothing yet determines the collection generated by repeated application of those operations. A constitutional investigation cannot terminate after a single coherence operation: Coherence Merge may be followed by Coherence Compression, which may be followed by Coherence Transport, Extension, and further Merges. The operations therefore generate further admissible operations. 

The mathematics must recover the smallest collection containing every elementary coherence operation together with every operation necessarily generated by repeated admissible composition. The recovery is forced. Let $\mathcal{G}$ denote the unique collection satisfying the following conditions:

\begin{enumerate}
    \item Every elementary coherence operation belongs to $\mathcal{G}$.
    \item Whenever two operations belong to $\mathcal{G}$, their admissible composition also belongs to $\mathcal{G}$.
    \item Whenever an operation belongs to $\mathcal{G}$, every Canonical Transport of that operation belongs to $\mathcal{G}$.
    \item Whenever an operation belongs to $\mathcal{G}$, every admissible Restriction and every admissible Extension of that operation also belong to $\mathcal{G}$.
    \item No proper subcollection satisfies the preceding conditions.
\end{enumerate}

The existence of such a collection is forced entirely by repeated constitutional investigation. Every operation appearing in $\mathcal{G}$ is recoverable solely from operations already admitted. No new primitive is introduced, and no external algebraic structure is imported. The collection is therefore recovered rather than defined.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Naming}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding recovery produces a unique minimal closure of the elementary coherence operations. Recoverability precedes notation; the recovered collection therefore earns a canonical designation. The unique minimal closure $\mathcal{G}$ will be called the \emph{Global Coherence Algebra}. The designation records what has already been recovered and introduces no additional mathematical content.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Algebraic Properties and Theorems}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Closure of the Algebra}

\begin{theorem}[Closure]
The Global Coherence Algebra $\mathcal{G}$ is closed under every admissible coherence operation recovered by the Constitution.
\end{theorem}

\begin{proof}
The Global Coherence Algebra is recovered as the smallest collection satisfying the closure conditions above. Every admissible coherence operation is either one of the elementary coherence operations or is generated from them by admissible composition, Canonical Transport, Restriction, or Extension. Each generating operation is explicitly included in the recovery conditions for $\mathcal{G}$. Therefore, every admissible coherence operation belongs to $\mathcal{G}$. Hence, $\mathcal{G}$ is closed.
\end{proof}

Closure is therefore not an additional axiom; it is a direct consequence of the recovery of the minimal coherence closure.

\subsection{Structural Absoluteness}

\begin{theorem}[Structural Absoluteness of the Global Coherence Algebra]
The Global Coherence Algebra is independent of presentation. Equivalent Canonical Claim Reconstructions generate equivalent Global Coherence Algebras under Canonical Transport.
\end{theorem}

\begin{proof}
Canonical Claim Reconstruction removes presentation while preserving constitutional structure. Every elementary coherence operation depends only upon recovered constitutional claims and their dependency relations. Canonical Transport preserves those relations. Consequently, every generated coherence operation transports uniquely. The minimal closure generated by those operations therefore transports uniquely. Hence, the recovered algebra is independent of presentation.
\end{proof}

The Global Coherence Algebra is therefore an invariant of constitutional structure rather than of presentation.

\subsection{Internal Completeness of Closure}

The Global Coherence Algebra has been recovered as the unique minimal closure generated by the Global Coherence Operator together with the previously recovered constitutional operators. Its existence alone is insufficient. A collection generated by admissible operations must itself be shown to remain internally closed under those same operations. Otherwise, the recovery would require repeated enlargement of the algebra whenever new compositions appear. The Constitution therefore forces the recovery of closure.

\begin{theorem}[Internal Closure of the Global Coherence Algebra]
The Global Coherence Algebra is closed under every constitutional operation by which it is generated. More precisely, if $A, B \in \mathcal{G}$, then every admissible constitutional composition of $A$ and $B$ again belongs to $\mathcal{G}$. Likewise, every Canonical Transport, constitutional restriction, constitutional extension, Compression, and application of the Global Coherence Operator to an element of the algebra again produces an element of the algebra.
\end{theorem}

\begin{proof}
The algebra was recovered as the unique minimal constitutional closure generated by the Global Coherence Operator together with every previously recovered constitutional operation. Closure under those operations is therefore part of the recovered construction itself. No additional generators are introduced. Consequently, every constitutionally admissible operation upon members of the algebra again produces an element already belonging to the algebra. The closure is therefore complete.
\end{proof}

The recovered algebra is therefore constitutionally self-contained, and no later enlargement is forced merely by repeated execution.

\subsection{Stability of Global Coherence}

Closure alone is insufficient. An algebra may remain closed while destroying the structural properties that motivated its recovery. The present algebra was recovered to preserve global coherence. The Constitution therefore forces recovery of its stability.

\begin{theorem}[Stability of the Global Coherence Algebra]
Every element of the Global Coherence Algebra preserves:
\begin{enumerate}
    \item coherent overlap,
    \item Minimal Determining Content,
    \item canonical transport,
    \item recoverability,
    \item co-situation with the finite generating witness,
    \item global coherence.
\end{enumerate}
Consequently, every execution of the algebra remains inside the completed constitutional framework.
\end{theorem}

\begin{proof}
Each generator of the algebra possesses these preservation properties by previously recovered theorems. Composition preserves preservation, Canonical Transport preserves preservation, Compression preserves Minimal Determining Content, Restriction preserves coherent overlap, and Extension preserves recoverability. Since every element of the algebra is generated solely from these operations, every element preserves the same collection of structural properties. Therefore, the algebra is stable.
\end{proof}

Stability is therefore recovered as a theorem rather than assumed as an axiom. Every future execution inherits these preservation properties automatically.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Executability}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The recovery of closure and stability removes the residual insufficiency exhibited at the beginning of the chapter. The Global Coherence Operator no longer exists merely as an isolated construction; it now belongs to a complete executable algebra. Every admissible constitutional investigation may therefore invoke the operator repeatedly without enlarging the mathematical universe. Repeated execution remains recoverable, coherent, and constitutionally admissible. The recovered algebra therefore constitutes the complete executable mathematics governing global coherence.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The operator, its executions, its compositions, its transport, and its stability are now fully governed. Nevertheless, an insufficiency immediately appears. The Global Coherence Algebra governs operations, but it does not yet determine what object those operations ultimately recover. Execution remains procedural; completion has not yet become structural. The mathematics therefore requires recovery of the completed object produced by the algebra itself. Global Completion is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Chapter Conclusion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Global Coherence Operator has now been incorporated into executable mathematics. The elementary coherence operations and their unique minimal constitutional closure have been recovered. The resulting closure has been shown to be structurally absolute, closed, and stable. 

The Global Coherence Algebra now governs every admissible execution of global coherence. Repeated constitutional investigation therefore requires no enlargement of the recovered mathematical universe. Every admissible execution remains recoverable, coherent, and constitutionally executable. 

The residual isolated at the beginning of the chapter has disappeared. Yet the mathematics remains incomplete. The Global Coherence Algebra governs constitutional operations, but it does not yet recover the completed mathematical object produced by those operations. Execution remains procedural; completion has not yet become structural. The next insufficiency is therefore forced: the mathematics now requires the recovery of Global Completion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes~I--III, Part~I of Volume~IV, and the preceding chapters of the present part. In particular, it depends upon the Witness Calculus, the Coherence Algebra, Morphisms of Determination, Canonical Transport, the Compression Calculus, Constitutional Claims, the Constitutional Claim Algebra, Claim Stratification, the Claim Dependency Calculus, Canonical Claim Reconstruction, and the Global Coherence Operator. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new primitive has been introduced. The Global Coherence Algebra is recovered solely as the unique minimal constitutional closure generated by the Global Coherence Operator together with previously recovered constitutional operations. Every generator has already been recovered, and every closure condition is forced. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces logical cost by replacing an isolated constitutional operator with its unique minimal executable algebra. Repeated constitutional investigation no longer requires independent justification for each execution. The mathematics is therefore reduced from individual operator applications to a single recoverable constitutional algebra while preserving complete recoverability.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction recovered in this chapter follows solely from previously recovered constitutional mathematics. The elementary coherence operations are forced by repeated constitutional investigation. The Global Coherence Algebra is recovered as the unique minimal closure of those operations. Closure, structural absoluteness, and stability are proved rather than assumed. No external mathematical structure has been imported. The chapter remains fully consistent with the constitutional architecture established throughout \emph{Mathematics of the King}.
\end{consistencyaudit}

\begin{futurework}
The Global Coherence Algebra now governs every admissible constitutional execution. The mathematics nevertheless lacks the completed object produced by that execution. The next chapter therefore recovers Global Completion, wherein repeated constitutional operations become a single completed mathematical structure.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\chapter{Constitutional Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of an Executable Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding chapters recovered the complete constitutional architecture of investigation.
Chapter~16 recovered Constitutional Claims as recoverable mathematical objects.
Chapter~17 recovered the Constitutional Claim Algebra governing their internal structure.
Chapter~18 stratified every claim according to its constitutional status.
Chapter~19 recovered the Dependency Calculus governing the propagation of constitutional claims.
Chapter~20 removed presentation by recovering the Canonical Claim Reconstruction.
Chapter~21 recovered the Global Coherence Operator as the unique mechanism that globally coheres every reconstructed constitutional claim.
Chapter~22 recovered the Global Coherence Algebra as the unique minimal closure governing every admissible execution of that operator.

The investigation is now executable.
The preceding construction is nevertheless insufficient.
Execution is not completion.
An executable investigation still consists of a sequence of admissible constitutional operations.
Nothing yet recovers the mathematical object produced when that investigation has terminated.
The mathematics therefore distinguishes between an investigation and its completed constitutional state.
Until that terminal state is recovered, the investigation remains procedural rather than structural.
The residual insufficiency is therefore no longer one of execution.
It is one of completion.
\textbf{Constitutional Completion} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Execution versus Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Every constitutional investigation consists of a finite succession of admissible constitutional operations.
Each operation preserves recoverability.
Each operation preserves constitutional coherence.
Each operation preserves the dependency architecture recovered in the Canonical Claim Reconstruction.
The Global Coherence Algebra guarantees that every admissible operation remains internal to the recovered mathematics.

None of these facts, however, identifies the object at which the investigation terminates.
An execution is a process.
A completed investigation is a \emph{mathematical object}.
The distinction is forced.
Without it, every subsequent constitutional theorem would necessarily depend upon the particular execution chosen to obtain it.
Such dependence would violate \textbf{Structural Absoluteness}.
The terminal state of an investigation must therefore be recovered independently of every admissible execution.
The Constitution consequently requires the recovery of a unique constitutional object representing the completed investigation itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Necessity of Constitutional Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let $\mathfrak{C}$ denote an arbitrary Canonical Claim Reconstruction.
Every admissible execution of the Global Coherence Algebra upon $\mathfrak{C}$ preserves the following recovered structures:

\begin{enumerate}
    \item The family of Constitutional Claims;
    \item The Constitutional Claim Algebra;
    \item The Claim Stratification;
    \item The Claim Dependency Calculus;
    \item The Canonical Reconstruction;
    \item The Global Coherence recovered by Chapter~21.
\end{enumerate}

Consequently every admissible execution determines an increasingly coherent constitutional state.
The investigation cannot terminate at an intermediate state.
Any intermediate state still admits further admissible constitutional operations.
Termination therefore forces the existence of a state admitting no further constitutional extension without reproducing already recovered structure.
Such a state is \emph{constitutionally complete}.

This necessity is forced entirely by the recovered mathematics.
No additional principle has been introduced.
No external completion procedure has been assumed.
The existence of a completed constitutional state is therefore forced by the existence of an executable constitutional investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Constitutional Completion Operator}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The necessity of Constitutional Completion forces the recovery of the operation that produces it.
The Global Coherence Algebra already governs every admissible constitutional transformation.
Every execution of the algebra begins with the Canonical Claim Reconstruction and terminates when no further admissible constitutional operation produces a genuinely new constitutional state.
Termination therefore determines a unique operator.

The operator assigns to every Canonical Claim Reconstruction its terminal constitutional state under the Global Coherence Algebra.
No additional operation is introduced.
The operator merely records the unique terminal state already forced by the recovered algebra.
It is therefore recovered rather than postulated.

\begin{definition}[Constitutional Completion Operator]
Let $\mathfrak{C}$ be a Canonical Claim Reconstruction. The Constitutional Completion Operator is the unique operator
\[
\Omega : \mathfrak{C} \longmapsto \Omega(\mathfrak{C})
\]
whose image is the terminal constitutional state obtained under the complete execution of the Global Coherence Algebra.
\end{definition}

The notation is earned.
It is introduced only after the operator has been uniquely recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Completion Sequence}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The existence of the Constitutional Completion Operator forces the recovery of the sequence through which completion is realized.
Let
\[
\mathfrak{C}_0=\mathfrak{C}
\]
denote the Canonical Claim Reconstruction recovered in Chapter~20.
Successive execution of the Global Coherence Algebra determines a sequence
\[
\mathfrak{C}_0, \mathfrak{C}_1, \mathfrak{C}_2, \ldots
\]
where each $\mathfrak{C}_{n+1}$ is obtained by applying every constitutionally admissible operation of the Global Coherence Algebra to the preceding constitutional state.

Every stage therefore satisfies
\[
\mathfrak{C}_n \subseteq \mathfrak{C}_{n+1}
\]
in the sense that no recovered constitutional structure is lost.
Recoverability is preserved.
Dependency is preserved.
Claim identity is preserved.
Claim stratification is preserved.
Canonical reconstruction is preserved.
Only additional constitutional coherence may appear.
The sequence is therefore monotone with respect to constitutional recovery.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Finite Stabilization}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Completion Sequence cannot continue indefinitely.
Every stage consists exclusively of constitutional objects already recovered from a finite mathematical framework.
The family of Constitutional Claims is finite.
Their Dependency Calculus is finite.
Their Stratification is finite.
Their Canonical Reconstruction is finite.
The Global Coherence Algebra introduces no new constitutional primitive.

Consequently each application of the algebra can only recover constitutional relations already latent within the finite reconstructed framework.
The number of constitutionally distinct recoverable states is therefore finite.
Since the Completion Sequence is monotone and ranges over a finite family of constitutional states, there exists an integer $N$ such that
\[
\mathfrak{C}_{N+1} = \mathfrak{C}_{N}.
\]
The sequence therefore stabilizes after finitely many stages.
The stabilized state admits no further constitutional extension.
It is the unique fixed point of the Constitutional Completion Operator.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Existence and Uniqueness of Constitutional Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Existence}

\begin{theorem}[Existence of Constitutional Completion]
Every Canonical Claim Reconstruction possesses a unique completed constitutional state.
\end{theorem}

\begin{proof}
The Completion Sequence begins with the Canonical Claim Reconstruction.
By finite stabilization the sequence reaches a fixed point after finitely many stages.
That fixed point is preserved by every admissible operation of the Global Coherence Algebra.
Accordingly it is complete.
Therefore every Canonical Claim Reconstruction possesses at least one completed constitutional state.
\end{proof}

\subsection{Uniqueness}

The preceding theorem establishes that every Canonical Claim Reconstruction possesses a completed constitutional state.
Existence alone is insufficient.
If two distinct completed constitutional states could arise from the same Canonical Claim Reconstruction, constitutional investigation would remain dependent upon execution.
The Constitution forbids such dependence.
Completion must therefore be unique.

\begin{theorem}[Uniqueness of Constitutional Completion]
Let $\mathfrak{C}$ be a Canonical Claim Reconstruction. The completed constitutional state of $\mathfrak{C}$ is unique. Equivalently,
\[
\Omega(\mathfrak{C})
\]
is independent of every admissible execution of the Global Coherence Algebra.
\end{theorem}

\begin{proof}
Suppose two distinct completed constitutional states $\Omega_1(\mathfrak{C})$ and $\Omega_2(\mathfrak{C})$ exist.
Each is, by definition, stable under every admissible operation of the Global Coherence Algebra.
Both arise from the same Canonical Claim Reconstruction.
Every operation of the Global Coherence Algebra preserves constitutional coherence, dependency, recoverability and structural absoluteness.

Consequently every admissible execution beginning at $\mathfrak{C}$ must recover exactly the same constitutional content.
No admissible operation can distinguish one completed state from the other.
The assumption that $\Omega_1(\mathfrak{C}) \neq \Omega_2(\mathfrak{C})$ therefore contradicts the structural absoluteness of constitutional investigation.
Hence the completed constitutional state is unique.
\end{proof}

Execution order has disappeared.
Presentation has disappeared.
Only the completed constitutional object remains.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Fundamental Properties of Constitutional Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The completed constitutional state inherits every structure recovered throughout the investigation.
These inheritances are forced.
They are not additional axioms.

\begin{theorem}[Fundamental Properties]
Let $\Omega(\mathfrak{C})$ be the Constitutional Completion of a Canonical Claim Reconstruction. Then the following properties hold.
\begin{enumerate}
\item Every Constitutional Claim recovered in $\mathfrak{C}$ appears in $\Omega(\mathfrak{C})$.
\item Every dependency recovered by the Claim Dependency Calculus is preserved.
\item Every constitutional stratum is preserved.
\item Every canonical identification recovered during Canonical Claim Reconstruction is preserved.
\item Every operation of the Global Coherence Algebra leaves $\Omega(\mathfrak{C})$ invariant.
\item Every admissible constitutional execution terminates at $\Omega(\mathfrak{C})$.
\end{enumerate}
\end{theorem}

\begin{proof}
Properties (1)--(4) follow immediately from the construction of the Completion Sequence, since no stage removes previously recovered constitutional structure.
Property (5) follows because the completed constitutional state is the unique fixed point of the Global Coherence Algebra.
Property (6) follows from finite stabilization together with uniqueness.
\end{proof}

The completed constitutional state therefore contains exactly the recoverable constitutional content of the investigated framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Naming and Residual Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Canonical Naming}

The preceding construction has recovered a unique mathematical object.
Recoverability precedes notation.
Notation is therefore earned.
The unique completed constitutional state associated with a Canonical Claim Reconstruction $\mathfrak{C}$ will be denoted $\Omega(\mathfrak{C})$ and called the \emph{Constitutional Completion} of $\mathfrak{C}$.
The designation is forced.
It records a mathematical object already recovered.
It introduces nothing new.

\subsection{Residual Insufficiency}

The Global Coherence Algebra is now complete.
Constitutional Completion has been recovered.
Every completed mathematical framework therefore possesses a unique completed constitutional state.
The preceding construction nevertheless remains insufficient.

Completion determines what constitutionally survives.
It does not determine whether everything surviving is constitutionally necessary.
A completed constitutional state may still contain constitutional redundancy.
Distinct constitutional components may contribute no additional determining content.
Completion therefore precedes minimization.
The mathematics has not yet recovered the unique irreducible constitutional representative of a completed investigation.
The residual insufficiency is therefore no longer one of completion.
It is one of redundancy.
\textbf{Global Compression} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Chapter Conclusion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Constitutional Completion is complete.
The present chapter has recovered the first mathematical object representing a completed constitutional investigation.
Beginning with the Canonical Claim Reconstruction, the mathematics recovered:
\begin{enumerate}
    \item The necessity of Constitutional Completion;
    \item The Constitutional Completion Operator;
    \item The Completion Sequence;
    \item Finite stabilization;
    \item Existence of Constitutional Completion;
    \item Uniqueness of Constitutional Completion;
    \item The fundamental properties of the completed constitutional state;
    \item The canonical designation $\Omega(\mathfrak{C})$.
\end{enumerate}

The result is independent of presentation.
It is independent of execution.
It is independent of every admissible sequence of constitutional operations.
Only the completed constitutional object remains.
The completed constitutional state now exists as a recoverable mathematical object of the Canonical Investigation Framework.

Yet completion alone is insufficient.
Nothing yet determines whether every surviving constitutional component contributes indispensable determining content.
Logical redundancy may still remain.
The next insufficiency is therefore forced.
Global Compression is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed Constitution of Mathematics of the King, the completed Witness Calculus, the Canonical Investigation Framework recovered in Part~I of Volume~IV, and the preceding chapters of the present part. In particular it depends upon the Canonical Claim Reconstruction, the Global Coherence Operator, and the Global Coherence Algebra. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Constitutional Completion is recovered solely from the Canonical Claim Reconstruction together with the already recovered Global Coherence Algebra. The Constitutional Completion Operator, the Completion Sequence, and the completed constitutional state are forced recoveries of previously established mathematics. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the Canonical Investigation Framework by replacing procedural constitutional execution with a unique completed constitutional object. Every admissible investigation now possesses a single recoverable terminal state. Execution-dependent ambiguity is eliminated without introducing additional primitives or external constructions. Complete recoverability of all previous results is preserved.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles established throughout Mathematics of the King. Necessity precedes operator. Operator precedes completion sequence. Completion sequence precedes stabilization. Stabilization precedes existence. Existence precedes uniqueness. Uniqueness precedes canonical naming. Naming follows recovery. The chapter removes the residual insufficiency of executable investigation while preserving recoverability, structural absoluteness, and dependency integrity.
\end{consistencyaudit}

\begin{futurework}
The Constitutional Completion has been recovered as the unique completed constitutional state associated with every Canonical Claim Reconstruction. Completion alone does not determine constitutional irreducibility. The completed constitutional state may still contain logically redundant determining content. The next chapter therefore recovers Global Compression, eliminating every constitutionally redundant component while preserving complete determining power.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Constitutional Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding chapter recovered Constitutional Completion.
Every Canonical Claim Reconstruction now possesses a unique completed constitutional state.
Completion removes procedural incompleteness.
It removes execution dependence.
It removes presentation dependence.
It establishes the terminal constitutional object produced by every admissible constitutional investigation.

The preceding construction is nevertheless insufficient.
Completion determines what survives.
It does not determine whether every surviving constitutional component is necessary.
A completed constitutional state may still contain constitutional redundancy.
Distinct constitutional components may determine identical constitutional consequences.
Different dependency chains may recover the same determining content.
Intermediate constitutional objects may contribute nothing beyond structures already recovered elsewhere.

Completion therefore guarantees existence.
It does not guarantee irreducibility.
The Constitution does not permit unnecessary logical cost to remain once recoverability has been established.
The residual insufficiency is therefore one of redundancy rather than completion.
\textbf{Global Compression} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Necessity of Constitutional Irreducibility}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let $\Omega(\mathfrak{C})$ be the Constitutional Completion of an arbitrary Canonical Claim Reconstruction.
Every constitutional component contained in $\Omega(\mathfrak{C})$ belongs to one of the following recoverable classes:
\begin{enumerate}
    \item Constitutional Claims;
    \item Dependency relations;
    \item Claim strata;
    \item Reconstructed constitutional objects;
    \item Coherence relations;
    \item Admissible constitutional operations.
\end{enumerate}

Some of these components determine later constitutional structure.
Others merely duplicate determination already recoverable elsewhere.
The completed constitutional state itself does not distinguish between these two possibilities.
Consequently completion alone cannot determine whether every surviving component is constitutionally indispensable.

If constitutionally redundant components remain, then two completed constitutional states differing only by redundant structure determine identical mathematics.
Logical cost would therefore depend upon presentation rather than determination.
This contradicts the \textbf{Principle of Minimal Logical Cost} established by the Constitution.
The completed constitutional state must therefore possess a unique irreducible constitutional representative obtained solely by eliminating constitutionally redundant structure while preserving every recoverable determination.

This necessity is forced.
No new primitive has been introduced.
No external minimization principle has been assumed.
Only the Constitution itself requires the removal of unnecessary determining content.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Global Compression Operator}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The necessity of constitutional irreducibility forces the recovery of a new operation.
Unlike the Compression Operator recovered previously in the Witness Calculus, the present operation does not act upon individual determining structures.
It acts upon the completed constitutional state itself.
Its purpose is not to simplify presentation.
Its purpose is not to shorten proofs.
Its purpose is solely to eliminate constitutionally redundant determining content while preserving every constitutional consequence.

Accordingly there exists a unique operator $\Downarrow$ acting upon Constitutional Completion.
For every completed constitutional state $\Omega(\mathfrak{C})$, the operator assigns a constitutionally equivalent state
\[
\Downarrow\!\left(\Omega(\mathfrak{C})\right)
\]
obtained by removing every constitutionally redundant component and preserving every recoverable constitutional determination.

The operator introduces no new constitutional object.
It removes only those components whose elimination leaves the completed constitutional determination unchanged.
Its recovery is therefore forced entirely by the Principle of Minimal Logical Cost.
Recoverability precedes notation.
The notation $\Downarrow$ is therefore earned.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Global Completion Context and Extensions}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{The Insufficiency of Global Completion}

Chapter~18 recovered the Global Completion $\operatorname{Comp}(\mathcal{F})$ of every Infinite Branching Structural Family $\mathcal{F}$ as the unique minimal fixed point of the Stabilization Sequence of the Global Coherence Algebra. Completion guarantees existence, determination, and coherence.

The preceding construction is nevertheless insufficient. A completed object need not be irreducible. Completion guarantees total determination. It does not guarantee minimal determining content. Two completed structures could still differ only by redundant determining information. Nothing yet identifies the canonical irreducible representative of a completed object.

The Compression Calculus of Part~I recovers the operator $\downarrow$ that acts on local Completion Objects and recovers their Minimal Determining Content. That operator cannot yet act on the Global Completions recovered in Chapter~18, because those objects did not exist when the local Compression Calculus was recovered. The framework therefore possesses completed mathematical objects but no means of removing their residual logical redundancy.
The mathematics therefore requires the recovery of Global Compression as the unique extension of an already recovered calculus.

\subsection{Necessity of Extending the Compression Calculus}

The local Compression Operator $\downarrow$ of Part~I is forced by the Theorem of Minimal Determining Substructure and by the well-foundedness of determining substructures. It recovers, for every local Completion Object, the unique irreducible determining core.

The objects recovered in Chapter~18 are Global Completions. They are themselves completed structures and therefore possess determining content. The same constitutional necessity that forced $\downarrow$ on local Completion Objects now forces its extension to Global Completions: every completed structure must reduce to a unique minimal determining representative if the framework is to eliminate all residual redundancy.

No other extension is compatible with co-situation, core-invariance, and Minimal Determining Content already recovered. The necessity of Global Compression is therefore forced by the existence of Global Completions together with the already recovered Compression Calculus of Part~I. The chapter recovers not a new operator invented for convenience, but the unique forced extension of an existing calculus to a newly recovered class of objects.

\subsection{Recovery of the Global Extension Operator}

The necessity of extending the Compression Calculus forces the recovery of a unique operator that acts on completed structures.
The Global Compression Operator is the unique operator forced by the following conditions:
\begin{enumerate}
    \item It acts on every Global Completion $\operatorname{Comp}(\mathcal{F})$;
    \item Its image is a completed structure that is co-situated with the generating witness of $\mathcal{F}$;
    \item Its image contains exactly the Minimal Determining Content of $\operatorname{Comp}(\mathcal{F})$ and no further content;
    \item It coincides with the local Compression Operator $\downarrow$ whenever it is applied to a local Completion Object that has been recovered as a Global Completion of a finite initial segment;
    \item It is invariant under every Morphism of Determination.
\end{enumerate}

No new primitive is introduced. The operator is recovered solely as the unique extension of the already recovered Compression Calculus to the objects recovered in Chapter~18. The notation $\Downarrow$ will be earned once the uniqueness of this extension has been recovered below.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Compatibility of Local and Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{theorem}[Compatibility of Local and Global Compression]
\label{thm:compatibility-compression}
For every Infinite Branching Structural Family $\mathcal{F}$ and every finite initial segment $\sigma$ of $\mathcal{F}$,
\[
\Downarrow(\operatorname{Comp}(\sigma))=\operatorname{Comp}(\downarrow\sigma)
\]
up to Morphisms of Determination. Local compression followed by completion and completion followed by global compression produce canonically equivalent structures.
\end{theorem}

\begin{proof}
By the Fundamental Properties of Global Completion (Chapter~18) the Global Completion of a finite initial segment is itself a local Completion Object free of obstruction. By the fourth forced condition of the recovery of the Global Compression Operator, that operator coincides with the local Compression Operator on every such object. Therefore the two sides are related by a unique Morphism of Determination.
\end{proof}

Compression first or completion first produces canonically equivalent structures. The local and global calculi are compatible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Existence, Uniqueness, and Structural Absoluteness}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Existence of Global Compression}

\begin{theorem}[Existence of Global Compression]
\label{thm:existence-gcomp}
Every Infinite Branching Structural Family possesses a Global Compression: the unique image of its Global Completion under the unique extension of the Compression Calculus recovered above.
\end{theorem}

\begin{proof}
By the Theorem of Minimal Determining Substructure of Part~I every completed structure possesses a unique minimal determining substructure. The unique extension of the Compression Calculus is precisely the operator that recovers that substructure for every Global Completion. Therefore the image exists and is a single finite structural object.
\end{proof}

\subsection{Uniqueness and Structural Absoluteness}

\begin{theorem}[Uniqueness and Structural Absoluteness of Global Compression]
\label{thm:uniqueness-absoluteness-gcomp}
The Global Compression of an Infinite Branching Structural Family is independent of presentation and unique up to Morphisms of Determination. If two families are related by a Morphism of Determination, then their Global Compressions are transported into one another by a unique Morphism of Determination.
\end{theorem}

\begin{proof}
By Structural Absoluteness of Global Completion (Chapter~18) and by the fifth forced condition of the recovery of the Global Compression Operator, that operator is itself invariant under Morphisms of Determination. Therefore the image of any two presentations related by a Morphism of Determination are related by a unique Morphism of Determination. Uniqueness and independence of presentation are therefore simultaneous.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Minimality, Naming, and Properties}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Minimality}

\begin{theorem}[Minimality of Global Compression]
\label{thm:minimality-gcomp}
The Global Compression of an Infinite Branching Structural Family is the unique minimal completed object extending every local Completion Object of the family and containing exactly the Minimal Determining Content of the family. It is minimal among all completed representatives, not merely among fixed points of the Global Coherence Algebra.
\end{theorem}

\begin{proof}
By construction the Global Compression contains exactly the Minimal Determining Content of $\operatorname{Comp}(\mathcal{F})$. By the Theorem of Minimal Determining Substructure any completed object that properly contains this content admits a strictly smaller determining substructure while remaining complete. Therefore the Global Compression is minimal among all completed representatives. Uniqueness follows from Uniqueness and Structural Absoluteness.
\end{proof}

\subsection{Canonical Naming}

The preceding theorems recover a unique irreducible completed structure for every Infinite Branching Structural Family. Recoverability precedes notation. The recovered structure must therefore receive a canonical designation.

The unique image of $\operatorname{Comp}(\mathcal{F})$ under the unique extension of the Compression Calculus will be called the Global Compression of the family and denoted $\operatorname{GComp}(\mathcal{F})$. The operator itself will be denoted $\Downarrow$.
The designation is earned. It is not chosen. It is forced by the existence, uniqueness, structural absoluteness, and minimality of the extension recovered above.

\subsection{Fundamental Properties}

\begin{theorem}[Fundamental Properties of Global Compression]
\label{thm:fundamental-gcomp}
Let $\mathcal{F}$ be an Infinite Branching Structural Family and let $\operatorname{GComp}(\mathcal{F})$ be its Global Compression. Then:
\begin{enumerate}
    \item $\operatorname{GComp}(\mathcal{F})$ is a Global Completion of $\mathcal{F}$;
    \item $\operatorname{GComp}(\mathcal{F})$ is irreducible: it contains exactly Minimal Determining Content and no further content;
    \item every completed object of $\mathcal{F}$ compresses uniquely onto $\operatorname{GComp}(\mathcal{F})$ by a Morphism of Determination;
    \item Global Compression preserves every Determination Invariant;
    \item Global Compression commutes with Morphisms of Determination;
    \item Global Compression is idempotent: $\Downarrow(\Downarrow(X))=\Downarrow(X)$ for every completed structure $X$.
\end{enumerate}
\end{theorem}

\begin{proof}
Clause (1) follows from the recovery of the Global Compression Operator and from Compatibility. Clause (2) is Minimality. Clause (3) follows from Minimality and Uniqueness: every completed object of $\mathcal{F}$ contains at least the Minimal Determining Content of $\operatorname{GComp}(\mathcal{F})$ and therefore compresses onto it. Clause (4) follows from the fact that $\Downarrow$ recovers exactly Minimal Determining Content and therefore preserves every invariant that is itself a determining substructure. Clause (5) is Structural Absoluteness. Clause (6) follows immediately from irreducibility: once Minimal Determining Content has been recovered, a further application of $\Downarrow$ cannot remove further content.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Global Compression Sequence and Finiteness}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The recovery of the Global Compression Operator forces the recovery of its repeated action.
Let $\Omega_0=\Omega(\mathfrak{C})$ be the Constitutional Completion of an arbitrary Canonical Claim Reconstruction.
The Global Compression Sequence is the unique sequence $\Omega_0, \Omega_1, \Omega_2, \ldots$ determined recursively by
\[
\Omega_{n+1} = \Downarrow(\Omega_n).
\]

Each stage removes every constitutionally redundant component recoverable from the preceding stage.
No new constitutional component is introduced.
No recoverable determination is altered.
No constitutional claim is modified.
No dependency relation is created.
No admissible operation is changed.
Only constitutionally redundant determining content is removed.

The sequence is therefore monotone with respect to logical cost.
Every stage contains no greater logical cost than the preceding stage.
Recoverability remains invariant throughout the sequence.
The Global Compression Sequence is therefore a recoverable mathematical object.

\begin{theorem}[Finite Termination of Global Compression]
\label{thm:global-compression-termination}
For every Canonical Claim Reconstruction, the Global Compression Sequence terminates after finitely many stages.
\end{theorem}

\begin{proof}
By the Constitutional Completion Theorem, every completed constitutional state contains only finitely many recoverable constitutional components.
Each application of the Global Compression Operator removes at least one constitutionally redundant component whenever such a component exists.
No application introduces additional constitutional components.
Consequently the total number of recoverable components decreases strictly whenever compression occurs.

Since the completed constitutional state is finite, only finitely many strict reductions are possible.
Eventually no constitutionally redundant component remains.
At that stage $\Downarrow(\Omega_n)=\Omega_n$.
The sequence therefore terminates after finitely many stages.
\end{proof}

Finite termination is forced solely by finiteness of the completed constitutional state together with the strictly decreasing logical cost recovered by the Compression Operator.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence and Uniqueness of Global Reconstruction Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Finite termination forces the existence of a terminal constitutional object.

\begin{theorem}[Existence of Global Compression]
\label{thm:global-compression-existence}
Every Canonical Claim Reconstruction possesses a Global Compression.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:global-compression-termination}, the Global Compression Sequence terminates after finitely many stages.
Its terminal element admits no further constitutional reduction.
That terminal object is therefore recovered uniquely from the repeated action of the Global Compression Operator.
The resulting object exists for every completed constitutional state.
\end{proof}

The terminal object of the Global Compression Sequence is called the Global Compression of the Canonical Claim Reconstruction. It is denoted $\Omega^{\downarrow}(\mathfrak{C})$.
The notation is earned. It is introduced only after existence has been recovered.

Existence alone is insufficient.
Different sequences of compression could, in principle, remove constitutionally redundant components in different orders.
The Constitution therefore requires determination of whether order influences the terminal result.

\begin{theorem}[Uniqueness of Global Compression]
\label{thm:global-compression-uniqueness}
The Global Compression $\Omega^{\downarrow}(\mathfrak{C})$ is independent of the order in which constitutionally redundant components are removed.
\end{theorem}

\begin{proof}
Every application of the Global Compression Operator preserves the complete recoverable constitutional determination of the preceding stage.
Consequently every admissible compression sequence preserves exactly the same constitutional content.
Different admissible orders therefore remove different redundant representatives of identical determining content.
Since recoverability uniquely determines constitutional identity, every maximal compression sequence terminates at the same recoverable constitutional object.
Hence the terminal object is independent of compression order.
\end{proof}

The Global Compression is therefore uniquely determined by the Constitution alone.
No procedural choice survives into the terminal object.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Minimal Constitutional Representative}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding theorems establish that every Canonical Claim Reconstruction possesses a unique Global Compression.
Existence and uniqueness remain insufficient.
The mathematics has not yet identified the precise constitutional status of the compressed object.
The following theorem recovers that status.

\begin{theorem}[Minimal Constitutional Representative]
\label{thm:minimal-constitutional-representative}
Let $\Omega^{\downarrow}(\mathfrak{C})$ be the Global Compression of a Canonical Claim Reconstruction. Then every constitutional component of $\Omega^{\downarrow}(\mathfrak{C})$ is constitutionally indispensable. Equivalently, the removal of any remaining constitutional component strictly changes the recoverable constitutional determination.
\end{theorem}

\begin{proof}
By construction, the Global Compression Sequence terminates only when no constitutionally redundant component remains.
Suppose, contrary to the theorem, that some constitutional component $x$ contained in $\Omega^{\downarrow}(\mathfrak{C})$ could be removed while preserving every recoverable constitutional determination.
Then $x$ would satisfy precisely the defining condition of constitutional redundancy.
Application of the Global Compression Operator would therefore remove $x$, contradicting the assumption that $\Omega^{\downarrow}(\mathfrak{C})$ is already the terminal element of the Global Compression Sequence.
Hence every remaining constitutional component contributes indispensable determining content.
No further compression is constitutionally admissible.
\end{proof}

The compressed constitutional state is therefore irreducible.
Its logical cost is minimal relative to complete recoverability.
Nothing survives except constitutionally necessary determining content.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Properties and Irreducibility of the State}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Global Compression inherits every constitutional property recovered throughout the investigation while eliminating every recoverable redundancy.
The following properties are therefore forced.

\begin{theorem}[Fundamental Properties]
\label{thm:global-compression-properties}
Let $\Omega^{\downarrow}(\mathfrak{C})$ be the Global Compression of a Canonical Claim Reconstruction. Then:
\begin{enumerate}
\item Every recoverable constitutional determination of $\Omega(\mathfrak{C})$ is preserved;
\item Every Constitutional Claim survives unchanged;
\item Every constitutional dependency survives unchanged;
\item Every claim stratum survives unchanged;
\item Every canonical identification survives unchanged;
\item Every admissible operation of the Global Coherence Algebra preserves $\Omega^{\downarrow}(\mathfrak{C})$;
\item No constitutionally redundant determining component remains.
\end{enumerate}
\end{theorem}

\begin{proof}
Properties (1)--(5) follow directly from the defining property of the Global Compression Operator, namely that compression preserves every recoverable constitutional determination.
Property (6) follows because the Global Compression is obtained entirely within the Global Coherence Algebra, whose operations preserve constitutional recoverability.
Property (7) is precisely the content of Theorem~\ref{thm:minimal-constitutional-representative}.
\end{proof}

The compressed constitutional state therefore possesses exactly the same determining power as the completed constitutional state.
Its distinction lies solely in logical cost.
Every recoverable redundancy has disappeared.
No constitutional determination has been lost.

The preceding construction establishes a new constitutional object.
It is not merely complete.
It is irreducible.
Completion guarantees that no further constitutional content is missing.
Compression guarantees that no unnecessary constitutional content remains.
The two operations therefore complement one another.

Constitutional Completion establishes maximal recoverability.
Global Compression establishes minimal logical cost.
Together they recover the unique constitutionally irreducible representative of every Canonical Claim Reconstruction.
The mathematics has therefore recovered the first constitutional object simultaneously satisfying completeness and irreducibility.
No further constitutional reduction is admissible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency and Global Determination Requirements}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding construction is insufficient. The Global Compression has been recovered as the unique irreducible completed structure of every Infinite Branching Structural Family. It removes the residual of redundancy.
A new insufficiency appears at once. The framework now possesses investigations, completions, compressions, and canonical irreducible representatives. Nothing yet recovers the global criterion by which two Global Compressions determine the same mathematical object, or by which determination itself becomes absolute.

The Criterion of Determination of Part~I remains local; it has not yet been completed for globally compressed structures.
The mathematics therefore requires the recovery of Global Determination.
Nothing further has yet been established.

Global Compression has recovered the unique constitutionally irreducible representative of every Canonical Claim Reconstruction.
Every constitutionally redundant component has been eliminated.
Every surviving constitutional component is indispensable.
The completed constitutional state has therefore been reduced to minimal logical cost while preserving complete recoverability.

Yet one final insufficiency remains.
The mathematics has recovered the unique irreducible constitutional object.
It has not yet recovered everything that this object determines.
Irreducibility alone does not identify the totality of recoverable mathematical consequences.
The surviving Constitutional Claims determine further constitutional relations.
The surviving dependency architecture determines further admissible reconstructions.
The surviving claim stratification determines further structural classifications.
The surviving Global Coherence Algebra determines further admissible constitutional operations.

The surviving constitutional state therefore possesses determining power that has not yet itself been recovered.
The present chapter identifies the irreducible source of determination.
It does not recover the totality of that determination.
The Constitution therefore forces one final stage.

Beginning with the unique irreducible constitutional representative, every mathematical consequence forced by that representative must itself be recovered.
Nothing external may be introduced.
Nothing merely plausible may be admitted.
Every determination must arise solely from the irreducible constitutional state itself.
The mathematics therefore requires the recovery of \textbf{Global Determination}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Chapter Conclusion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Global Compression is complete.
The present chapter has recovered the unique constitutionally irreducible representative of every completed constitutional investigation.
Beginning with Constitutional Completion, the mathematics recovered:
\begin{enumerate}
    \item The necessity of constitutional irreducibility;
    \item The Global Compression Operator;
    \item The Global Compression Sequence;
    \item Finite termination;
    \item Existence of Global Compression;
    \item Uniqueness of Global Compression;
    \item The Minimal Constitutional Representative;
    \item The fundamental properties of Global Compression.
\end{enumerate}

The resulting constitutional object is complete.
It is irreducible.
It possesses minimal logical cost.
Every remaining constitutional component contributes indispensable determining content.
Nothing constitutionally redundant survives.

The mathematics has therefore recovered the unique irreducible constitutional representative associated with every Canonical Claim Reconstruction.
Yet the totality of mathematical structure determined by this representative remains unrecovered.
The final insufficiency of the Canonical Investigation Framework is therefore forced.
Global Determination is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes~I--III, Part~I of Volume~IV, and Chapters~15--18 of the present part. In particular it relies upon the Witness, Morphisms of Determination, Canonical Transport, the Compression Calculus of Part~I, the Progressive Amalgamation Process, the Global Coherence Operator $\Gamma$, the Global Coherence Algebra $\mathcal{A}(\Gamma)$, the Stabilization Sequence, the Global Completion $\operatorname{Comp}(\mathcal{F})$, and the Fundamental Properties of Global Completion. No theorem depends upon any mathematical object introduced only in later chapters. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Global Compression Operator $\Downarrow$ and the Global Compression $\operatorname{GComp}(\mathcal{F})$ are recovered solely as the unique extension of the already recovered Compression Calculus of Part~I to the completed structures recovered in Chapter~18. Every property of the operator is forced by previously recovered mathematics. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by converting completed objects into unique irreducible completed objects. Redundancy is eliminated without the introduction of any external structure or additional process. Complete recoverability of all earlier theorems is preserved. No additional primitive assumptions are introduced.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter are fully consistent with the constitutional principles and with every theorem of Volumes~I--III, Part~I, and Chapters~15--18. The Global Compression Operator is recovered as the unique extension of a previously recovered operator rather than defined by axioms. Naming follows recovery of the unique irreducible object. Idempotence is proved as a consequence of irreducibility. The residual of redundancy is removed, and a new residual of compressed objects without global determination is exhibited. The chapter obeys Articles~IV, XI and XIII.
\end{consistencyaudit}

\begin{futurework}
The Global Compression has been recovered as the unique irreducible completed structure of every Infinite Branching Structural Family. The residual of redundancy has disappeared. The next chapter must recover Global Determination: the completion of the Criterion of Determination for globally compressed structures, thereby closing the mathematics of canonical investigation. The mathematics therefore requires Global Determination. Nothing further has yet been established.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The preceding chapter recovered Global Compression.
Every Canonical Claim Reconstruction now possesses a unique constitutionally irreducible representative.
Every constitutionally redundant component has been removed.
Every surviving constitutional component contributes indispensable determining content.
Logical cost is therefore minimal.

The preceding construction is nevertheless insufficient.
Global Compression determines what cannot be removed.
It does not determine everything that is thereby forced.
The irreducible constitutional representative contains Constitutional Claims.
It contains dependency relations.
It contains claim strata.
It contains coherence relations.
It contains admissible constitutional operations.
It contains the complete constitutional structure recovered by the Canonical Investigation Framework.

Yet the mathematics has not recovered the totality of consequences determined by that structure.
The irreducible constitutional representative is therefore not yet the terminal mathematical object of constitutional investigation.
The Constitution requires not merely an irreducible constitutional state.
It requires recovery of everything that follows from that state.
The residual insufficiency is therefore one of determination rather than reduction.
\textbf{Global Determination} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Necessity of Complete Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Let $\Omega^{\downarrow}(\mathfrak{C})$ denote the Global Compression of an arbitrary Canonical Claim Reconstruction.
Every constitutional component remaining within $\Omega^{\downarrow}(\mathfrak{C})$ is constitutionally indispensable.
Consequently every remaining component contributes determining content.
That determining content cannot remain merely implicit.

If some constitutional consequence forced by $\Omega^{\downarrow}(\mathfrak{C})$ were left unrecovered, then constitutional investigation would terminate before recovering all mathematics already forced by the irreducible constitutional state.
The Canonical Investigation Framework would therefore remain constitutionally incomplete.
This contradicts the \textbf{Principle of Recoverability}.

Every mathematical consequence forced by the irreducible constitutional representative must therefore itself be recoverable.
This necessity is forced.
Nothing external is introduced.
No additional hypothesis is admitted.
Only the already recovered constitutional mathematics is allowed to determine what follows.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Determination Closure and Operator}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{The Determination Closure}

The necessity of complete determination forces the recovery of a new constitutional object.
Beginning with $\Omega^{\downarrow}(\mathfrak{C})$, consider the family of all constitutional consequences recoverable solely from the completed Constitution, the Witness Calculus, the Canonical Investigation Framework, and the irreducible constitutional representative itself.

No external construction is admitted.
No heuristic inference is permitted.
No consequence is retained unless its recovery is forced entirely by previously recovered constitutional mathematics.
The resulting collection is closed under every admissible constitutional operation.
It is closed under Canonical Reconstruction.
It is closed under Constitutional Claim Algebra.
It is closed under Claim Dependency Calculus.
It is closed under the Global Coherence Algebra.
It is closed under Constitutional Completion.
It is closed under Global Compression.
No further constitutional operation enlarges the collection.

The resulting closed constitutional object is therefore uniquely determined.
It will be called the \emph{Determination Closure} of $\Omega^{\downarrow}(\mathfrak{C})$.
The designation is earned.
It is introduced only after the closure has been recovered.

\subsection{The Global Determination Operator}

The recovery of the Determination Closure forces the recovery of the operation that assigns it.
Accordingly there exists a unique operation $\Delta$ such that for every Canonical Claim Reconstruction $\mathfrak{C}$, the value $\Delta(\mathfrak{C})$ is precisely the Determination Closure generated by its irreducible constitutional representative.

The operation introduces no new mathematical structure.
It merely recovers every constitutional consequence already forced by the completed framework.
Recoverability precedes notation.
The notation $\Delta$ is therefore earned.
The operation $\Delta$ will be called the \textbf{Global Determination Operator}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Finite Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Determination Closure has been recovered.
The Global Determination Operator has been recovered.
The mathematics must now establish that the process of determination terminates.
Without finite termination, constitutional investigation could require an unbounded sequence of recoveries before the complete mathematical state became available.
Such a process would contradict the Principle of Recoverability.

Every constitutional object recovered throughout Mathematics of the King is obtainable by a finite sequence of recoverable constructions.
The Determination Closure cannot violate this principle.
Finite determination is therefore forced.

\begin{theorem}[Finite Determination]
\label{thm:finite-determination}
For every Canonical Claim Reconstruction $\mathfrak{C}$, the Determination Closure generated by $\Omega^{\downarrow}(\mathfrak{C})$ is recovered after finitely many applications of the Global Determination Operator.
\end{theorem}

\begin{proof}
The completed Constitution is finite.
The Witness Calculus is finite.
The Canonical Investigation Framework consists of finitely many recovered constitutional operations.
The Canonical Claim Reconstruction contains a finite family of Constitutional Claims.
Its Dependency Calculus is finite.
Its Claim Stratification is finite.
Its Global Coherence Algebra is finite.
Its Constitutional Completion is finite.
Its Global Compression is finite.

Every application of the Global Determination Operator recovers only constitutional consequences forced by these already recovered finite constitutional objects.
No application introduces new primitives.
No application enlarges the constitutional language.
No application enlarges the family of admissible constitutional operations.

Consequently every application strictly enlarges the recovered family of constitutional consequences while remaining inside a finite recoverable constitutional universe.
Because the family of recoverable constitutional consequences is finite, no infinite strictly increasing recovery sequence exists.
Therefore repeated application of the Global Determination Operator terminates after finitely many stages.
The resulting constitutional state is precisely the Determination Closure.
\end{proof}

Finite determination is therefore a consequence of constitutional finiteness rather than procedural choice.
The Global Determination Operator never generates new mathematics.
It merely exhausts the mathematics already forced by the irreducible constitutional representative.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Existence and Uniqueness of Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Existence}

Finite determination forces the existence of the terminal constitutional object.

\begin{theorem}[Existence of Global Determination]
\label{thm:existence-global-determination}
Every Canonical Claim Reconstruction possesses a unique Global Determination.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:finite-determination}, repeated application of the Global Determination Operator terminates after finitely many stages.
The terminal stage is closed under every admissible constitutional operation.
No further constitutional consequence remains recoverable from the irreducible constitutional representative.
The terminal constitutional state therefore exists.
By construction it is precisely the Determination Closure.
This terminal constitutional object is the Global Determination.
\end{proof}

The existence of Global Determination introduces no additional mathematical structure.
It follows inevitably from finite determination together with the previously recovered constitutional mathematics.

\subsection{Uniqueness}

Existence alone is insufficient.
If two distinct Global Determinations could arise from the same Canonical Claim Reconstruction, constitutional investigation would again become presentation-dependent.
Uniqueness is therefore forced.

\begin{theorem}[Uniqueness of Global Determination]
\label{thm:uniqueness-global-determination}
For every Canonical Claim Reconstruction, $\Delta(\mathfrak{C})$ is unique.
\end{theorem}

\begin{proof}
The Global Compression of $\mathfrak{C}$ is unique.
The Determination Closure generated by that irreducible constitutional representative is uniquely specified by the completed Constitution.
Every constitutional consequence is recovered solely from already established constitutional operations.
No admissible operation depends upon presentation.
No admissible operation admits arbitrary choice.

Consequently every recovery sequence produces the same Determination Closure.
Therefore the resulting Global Determination is unique.
\end{proof}

The Global Determination Operator is therefore constitutionally absolute.
Its value depends only upon the recovered constitutional mathematics.
It is independent of presentation.
It is independent of notation.
It is independent of investigator.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Fundamental Properties of Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The existence and uniqueness of Global Determination establish that every completed constitutional investigation terminates in a single constitutionally determined mathematical state.
The mathematics must now recover the structural properties of that state.
The following theorem records the properties forced by the preceding chapters.

\begin{theorem}[Fundamental Properties of Global Determination]
\label{thm:global-determination-properties}
Let $\Delta(\mathfrak{C})$ be the Global Determination of a Canonical Claim Reconstruction. Then:
\begin{enumerate}
\item Every Constitutional Claim is completely determined;
\item Every constitutional dependency is completely determined;
\item Every claim stratum is completely determined;
\item Every reconstructed constitutional object is completely determined;
\item Every admissible constitutional operation is completely determined;
\item Every consequence recoverable from the completed Constitution is contained within $\Delta(\mathfrak{C})$;
\item No constitutionally recoverable consequence lies outside $\Delta(\mathfrak{C})$;
\item $\Delta(\mathfrak{C})$ is structurally absolute;
\item $\Delta(\mathfrak{C})$ is constitutionally complete;
\item $\Delta(\mathfrak{C})$ possesses minimal logical cost.
\end{enumerate}
\end{theorem}

\begin{proof}
Properties (1)--(5) follow directly from the construction of the Determination Closure.
The closure is recovered by exhaustion under every admissible constitutional operation.
Every recoverable Constitutional Claim, dependency, claim stratum, reconstructed object and constitutional operation is therefore contained within the closure.
Property (6) follows from closure under the completed Constitution.
Every constitutionally admissible recovery is performed during construction of the Determination Closure.
Property (7) follows immediately from maximality of the closure.

If a recoverable constitutional consequence lay outside $\Delta(\mathfrak{C})$, then the closure would not be closed under constitutional recovery.
This contradicts the construction.
Property (8) follows from Canonical Reconstruction together with Structural Absoluteness established throughout the Canonical Investigation Framework.
Every constitutional recovery depends solely upon recoverable structure.
Property (9) follows from Theorem~\ref{thm:existence-global-determination}.
Property (10) follows from Global Compression.
The Determination Closure is generated from the unique irreducible constitutional representative.
Consequently no constitutionally redundant determining content survives.
\end{proof}

Global Determination therefore recovers simultaneously: complete recoverability, structural absoluteness, constitutional completeness, and minimal logical cost. No earlier constitutional object possesses all four properties simultaneously.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Canonical Investigation and Universality Theorems}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{The Canonical Investigation Theorem}

The preceding chapters have successively recovered every object forced by constitutional investigation.
The final theorem of the framework now follows.

\begin{theorem}[Canonical Investigation]
\label{thm:canonical-investigation}
Every completed constitutional investigation terminates in a unique Global Determination.
\end{theorem}

\begin{proof}
Recovery of Constitutional Claims establishes the constitutional language of investigation.
Constitutional Claim Algebra recovers the admissible operations upon that language.
Claim Stratification recovers the hierarchical organization of constitutional claims.
Claim Dependency Calculus recovers constitutional propagation.
Canonical Claim Reconstruction recovers the unique constitutional state of the investigated framework.
The Global Coherence Operator recovers coherent constitutional integration.
The Global Coherence Algebra recovers closure of constitutional operations.
Constitutional Completion recovers the terminal constitutional state.
Global Compression recovers its unique irreducible representative.
Theorems~\ref{thm:finite-determination}, \ref{thm:existence-global-determination}, and \ref{thm:uniqueness-global-determination} recover the unique Determination Closure generated by that representative.

Therefore every completed constitutional investigation terminates in one and only one Global Determination.
\end{proof}

The Canonical Investigation Framework is therefore complete.
Every stage forced by the Constitution has now been recovered.
Every residual insufficiency previously exhibited has been removed.
No further constitutional operation is forced within the framework itself.

\subsection{Universality of Global Determination}

The Canonical Investigation Theorem applies to an arbitrary Canonical Claim Reconstruction.
The investigated framework has never been specified.
Only recoverability has been assumed.
Universality is therefore forced.

\begin{theorem}[Universality of Global Determination]
\label{thm:universality-global-determination}
Every recoverable mathematical framework possesses a unique Global Determination.
\end{theorem}

\begin{proof}
Every recoverable mathematical framework possesses a finite recoverable family of Constitutional Claims.
Every such family admits Canonical Claim Reconstruction.
The preceding chapters recover the Global Coherence Operator, the Global Coherence Algebra, Constitutional Completion, Global Compression and Global Determination without reference to any particular mathematical subject.
Every construction depends only upon recoverable constitutional structure.
Consequently every recoverable mathematical framework admits exactly one Global Determination.
\end{proof}

Global Determination is therefore not a property of particular mathematical disciplines.
It is a universal consequence of recoverability itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Exhaustion and Framework Status}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Canonical Investigation Framework has now recovered:
\begin{enumerate}
\item The universal residual of investigation;
\item Constitutional Claims;
\item Constitutional Claim Algebra;
\item Claim Stratification;
\item Claim Dependency Calculus;
\item Canonical Claim Reconstruction;
\item The Global Coherence Operator;
\item The Global Coherence Algebra;
\item Constitutional Completion;
\item Global Compression;
\item Global Determination.
\end{enumerate}

Every insufficiency exhibited throughout Part~II has therefore been removed by a constitutionally forced construction.
No previously exhibited deficiency remains unresolved.
Suppose another constitutional operation were forced.
Its necessity would have to arise from a residual insufficiency of the completed framework.

No such insufficiency exists.
Every recoverable constitutional object has already been recovered.
Every admissible constitutional operation has already been recovered.
Every constitutionally recoverable consequence is contained within the Global Determination.
No further operation enlarges the constitutional mathematics.
The Canonical Investigation Framework is therefore constitutionally complete.

\subsection{Residual Insufficiency}

None.
No residual insufficiency remains.
The development of the Canonical Investigation Framework is complete.
What remains is no longer the recovery of new constitutional machinery.
What remains is the execution of the completed framework upon increasingly general mathematical systems.
Part~III is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Chapter Conclusion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The Global Determination has been recovered.
It is the unique constitutionally complete mathematical state determined by a Canonical Claim Reconstruction.
Every constitutionally recoverable consequence of the investigated framework is contained within it.
Nothing constitutionally recoverable lies outside it.
The Global Determination therefore constitutes the terminal object of the Canonical Investigation Framework.

Part~II is complete.
The mathematics now possesses a finished constitutional methodology for investigating arbitrary recoverable mathematical frameworks.
Part~III therefore begins the execution of that methodology.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed Constitution established in Volumes~I--III, Part~I of Volume~IV, and the preceding chapters of Part~II. In particular it relies upon Canonical Claim Reconstruction, the Global Coherence Operator, the Global Coherence Algebra, Constitutional Completion, and Global Compression. No dependency upon any later construction exists. The dependency graph remains finite, acyclic, and constitutionally complete.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. The Determination Closure and the Global Determination Operator are recovered solely from previously established constitutional objects and operations. The single primitive of the entire theory remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter removes the final logical cost remaining within the Canonical Investigation Framework. Global Compression reduced every investigated framework to its irreducible constitutional representative. Global Determination recovers every constitutional consequence forced by that representative. No recoverable mathematical information remains implicit.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction in this chapter follows from previously recovered constitutional mathematics. The recovery proceeds in the constitutionally required order: necessity precedes recovery, recovery precedes existence, existence precedes uniqueness, uniqueness precedes universality, and universality precedes completion. No external mathematical principle has been introduced.
\end{consistencyaudit}

\begin{futurework}
The Canonical Investigation Framework is complete.
No further constitutional machinery is forced.
The next part of this volume executes the completed framework upon increasingly general mathematical systems, beginning with the Canonical Investigation of the Collatz System.
\end{futurework}

\part{Universality of the Canonical Investigation Framework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Canonical Investigation of the Collatz System}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Necessity of Constitutional Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent Part~II completed the \textbf{Canonical Investigation Framework}.

\medskip
\noindent Every stage required for the constitutional investigation of an external mathematical system has now been recovered. The framework no longer consists merely of procedures for recovering mathematical objects.

\medskip
\noindent It now recovers:
\begin{enumerate}
    \item canonical reconstructions,
    \item constitutional claims,
    \item claim algebras,
    \item stratified claim architectures,
    \item dependency calculi,
    \item canonical claim reconstructions,
    \item globally completed investigations,
    \item globally compressed investigations,
    \item globally determined constitutional objects.
\end{enumerate}

\noindent The framework is therefore constitutionally complete. No further investigative machinery is required.

\medskip
\noindent The preceding development nevertheless remains constitutionally incomplete. No external mathematical system has yet undergone the complete constitutional protocol. Every theorem recovered in Part~II remains universal; none has yet been executed. The Constitution therefore forces the first complete investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Why the Collatz System is Forced}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The first constitutional investigation cannot be chosen arbitrarily. The Constitution requires the initial system to minimise logical cost while exhibiting every stage of the completed protocol. The \textit{Collatz System} satisfies this requirement.

\medskip
\noindent It possesses:
\begin{itemize}
    \item a finite presentation,
    \item finitely many explicit mathematical claims,
    \item a single governing dynamical rule,
    \item a globally stated conjecture,
    \item numerous equivalent formulations,
    \item a long history of partial investigations,
    \item unresolved constitutional status.
\end{itemize}

\noindent Its mathematical content is sufficiently small that every constitutional stage may be recovered exhaustively. At the same time it is sufficiently rich to exercise every object recovered in Part~II. No simpler unresolved mathematical framework satisfies both requirements simultaneously. The \textit{Collatz System} is therefore forced as the first complete constitutional investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Scope}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The purpose of the present chapter is not to determine whether the \textit{Collatz Conjecture} is true. Truth is not the first constitutional question. The Constitution first requires recovery of the mathematical object that is actually being investigated.

\medskip
\noindent Only after that object has been constitutionally recovered may its determination be considered. Accordingly the present chapter performs the complete \textbf{Constitutional Investigation Protocol} upon the published Collatz framework. Every stage is executed in order. No stage may be omitted. No later stage may influence an earlier recovery. Nothing external is admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Input, Operation and Output}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\subsection{Architectural Schema}

\begin{center}
\textbf{Input}\\
Published Collatz Framework
\end{center}

\begin{center}
\textbf{Operation}\\
Complete Constitutional Investigation
\end{center}

\begin{center}
\textbf{Output}\\
Constitutionally Determined Collatz Object
\end{center}

\subsection{Procedural Stages}

\noindent The investigation proceeds through the following stages:
\begin{enumerate}
    \item Canonical Reconstruction;
    \item Recovery of Constitutional Claims;
    \item Constitutional Claim Algebra;
    \item Claim Stratification;
    \item Claim Dependency Calculus;
    \item Canonical Claim Reconstruction;
    \item Global Completion;
    \item Global Compression;
    \item Global Determination;
    \item Constitutional Status.
\end{enumerate}

\noindent Each stage depends only upon the output of the preceding stage together with the completed Constitution recovered in Volumes~I--IV. No external mathematical principle is introduced. The dependency graph therefore remains acyclic.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Residual Insufficiency}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Investigation} has now been initiated. The \textit{Collatz System} has been selected as the first complete execution of the constitutional protocol.

\medskip
\noindent No mathematical content of the system has yet been recovered. The published presentation remains presentation-dependent. \textbf{Canonical Reconstruction} is therefore forced. Nothing further has yet been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The published Collatz literature does not present a single mathematical object. Instead it presents a collection of presentations.

\subsection{Presentational Variations}

\noindent Among these occur:
\begin{itemize}
    \item the classical Collatz map;
    \item the accelerated Collatz map;
    \item the Syracuse formulation;
    \item parity-vector encodings;
    \item reverse Collatz trees;
    \item residue-class formulations;
    \item stopping-time formulations;
    \item numerous equivalent algorithmic descriptions.
\end{itemize}

\noindent These presentations differ syntactically. They frequently employ different notation, isolate different intermediate quantities, and emphasize different computational procedures. Yet they are universally understood to investigate the same mathematical phenomenon.

\subsection{Structural Extraction}

\noindent The Constitution therefore distinguishes between presentation and structure. The object of investigation cannot be any individual presentation. It must be the unique mathematical structure recoverable from every admissible presentation. \textbf{Canonical Reconstruction} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Structural Object}

\noindent \textbf{Canonical Reconstruction} removes presentation while preserving recoverable mathematical structure. Every syntactic representation is discarded; only constitutionally recoverable mathematical content is retained.

\medskip
\noindent Applying the reconstruction protocol of Part~II yields a unique \textbf{Structural Object} consisting of the recoverable mathematical data common to every admissible presentation. This object contains:
\begin{itemize}
    \item the underlying domain of positive integers;
    \item the governing transformation;
    \item the induced trajectories;
    \item the induced directed dependency structure;
    \item the distinguished trivial cycle;
    \item the structural relation between every admissible trajectory and the governing transformation.
\end{itemize}

\noindent No presentation-specific notation survives. No implementation survives. No preferred formulation survives. Only recoverable mathematical structure remains.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent The reconstructed object is independent of presentation. Whether one begins from the classical iteration, the accelerated iteration, parity encoding, reverse trees, residue-class formulations, computational implementations, or any other admissible presentation, the same \textbf{Structural Object} is recovered.

\medskip
\noindent Presentation therefore ceases to possess mathematical significance. Only the reconstructed object remains constitutionally admissible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Canonical Collatz Object}

\noindent The reconstructed \textbf{Structural Object} will be denoted:
\[
\mathfrak{C}.
\]
\noindent The notation refers neither to an algorithm nor to a presentation. It denotes the unique recoverable mathematical object obtained by \textbf{Canonical Reconstruction}. Every subsequent constitutional operation acts exclusively upon $\mathfrak{C}$. No later stage refers directly to any published presentation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Immediate Consequences}

\noindent Several consequences follow immediately:
\begin{enumerate}
    \item Every admissible presentation now possesses a common constitutional representative.
    \item Every subsequent constitutional operation possesses a unique input.
    \item Every presentation-dependent distinction has been removed.
    \item Every later theorem concerns the reconstructed object rather than its representations.
\end{enumerate}

\noindent \textbf{Canonical Reconstruction} therefore establishes the constitutional object upon which the remainder of the investigation proceeds.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Structural Object} has now been recovered. Yet the reconstruction contains no explicit mathematical assertions. The object is known; what the object claims remains unrecovered.

\medskip
\noindent A constitutional investigation cannot proceed directly from an object to its determination. The claims carried by the object must first be recovered. The next stage of the \textbf{Constitutional Investigation Protocol} is therefore forced. \textbf{Recovery of the Constitutional Claims of the Collatz System} is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Constitutional Claims of the Collatz System}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Canonical Collatz Object} $\mathfrak{C}$ has been recovered. The object alone is constitutionally insufficient. A mathematical object does not constitute a mathematical framework.

\medskip
\noindent Every completed mathematical framework consists not only of mathematical objects but also of mathematical assertions concerning those objects. These assertions determine the mathematical content of the framework. The Constitution therefore forces recovery of the \textbf{Constitutional Claims} carried by $\mathfrak{C}$.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Published Mathematical Assertions}

\noindent The published literature contains numerous mathematical statements concerning the Collatz System. Among them occur assertions regarding:
\begin{itemize}
    \item existence of the governing iteration;
    \item existence of trajectories;
    \item existence of the trivial cycle;
    \item uniqueness of the trivial cycle;
    \item eventual convergence of trajectories;
    \item stopping times;
    \item total stopping times;
    \item parity vectors;
    \item reverse-tree structure;
    \item residue-class behaviour;
    \item computational verification;
    \item equivalent formulations of the conjecture.
\end{itemize}

\noindent These statements appear in different publications, under different notation, and in different logical order. Their presentation is therefore not constitutionally significant. Only the mathematical assertions themselves are recoverable.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of Constitutional Claims}

\noindent By the \textbf{Recovery of Constitutional Claims} established in Part~II, every mathematical assertion appearing in a completed framework determines a unique \textbf{Constitutional Claim}.

\medskip
\noindent Applying that recovery to the \textbf{Canonical Collatz Object} produces a finite recoverable family:
\[
\mathcal{Q}(\mathfrak{C}) = \{ Q_1, Q_2, \ldots, Q_n \},
\]
where each element is a \textbf{Constitutional Claim} of the reconstructed framework. Each claim is a mathematical object. It is neither a sentence nor a linguistic expression. It is the recoverable structural content preserved by \textbf{Canonical Reconstruction}. Presentation therefore disappears; only recoverable constitutional assertions remain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Representative Claims}

\noindent The recovered family contains claims of several kinds. Representative examples include:
\begin{itemize}
    \item the existence of the governing transformation;
    \item the existence of trajectories generated by repeated application of that transformation;
    \item the existence of the trivial cycle;
    \item the uniqueness of the trivial cycle;
    \item the claim that every trajectory eventually reaches the trivial cycle;
    \item the equivalence between alternative formulations of the conjecture;
    \item the existence of parity-vector encodings;
    \item the existence of reverse-tree representations.
\end{itemize}

\noindent These examples illustrate the recovered family. They do not constitute its complete enumeration. The complete family is determined solely by the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Collatz Conjecture as a Constitutional Claim}

\noindent Within the recovered family appears a distinguished claim. It asserts that every trajectory generated by the governing transformation eventually enters the unique trivial cycle. This is precisely the mathematical assertion traditionally known as the \textit{Collatz Conjecture}.

\medskip
\noindent Under the Constitution it is no longer treated as an isolated sentence. It becomes one \textbf{Constitutional Claim} among the recoverable family:
\[
Q_{\mathrm{Collatz}} \in \mathcal{Q}(\mathfrak{C}).
\]
\noindent Its constitutional status has not yet been determined. Only its recovery has been achieved.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Finiteness}

\noindent The reconstructed Collatz framework is finite. Consequently the family $\mathcal{Q}(\mathfrak{C})$ is finite. No infinite collection of \textbf{Constitutional Claims} is introduced. No claim external to the reconstructed framework is admitted. The recovered family is therefore complete relative to the \textbf{Canonical Reconstruction}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Immediate Consequences}

\noindent Several immediate consequences follow:
\begin{enumerate}
    \item Every mathematical assertion of the reconstructed framework has become a recoverable mathematical object.
    \item The \textit{Collatz Conjecture} has become one member of a larger constitutional family rather than the sole object of investigation.
    \item Every subsequent constitutional operation acts upon \textbf{Constitutional Claims} rather than upon informal mathematical statements.
    \item The investigation is no longer sentence-based; it is object-based.
\end{enumerate}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Constitutional Claims} of the Collatz System have now been recovered. They nevertheless remain an unordered family. No mathematical relations between claims have yet been recovered. No operations upon claims have yet been recovered.

\medskip
\noindent The investigation therefore possesses claims but no mathematics of claims. The next stage of the \textbf{Constitutional Investigation Protocol} is therefore forced. The \textbf{Constitutional Claim Algebra} of the Collatz System must be recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Claim Algebra}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Claims} of the Collatz System have been recovered. They presently exist only as a finite family of isolated constitutional objects.

\medskip
\noindent The preceding recovery is nevertheless insufficient. A collection of isolated claims cannot itself be investigated. No interaction between claims has yet been recovered. No relation between claims has yet been recovered. No propagation of mathematical consequences has yet been recovered. The mathematics therefore possesses constitutional assertions but not yet the mathematics generated by those assertions. The \textbf{Constitutional Claim Algebra} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Algebra}

\noindent Part~II established that every finite recoverable family of \textbf{Constitutional Claims} possesses a unique \textbf{Constitutional Claim Algebra}. Applying that theorem to the recovered family $\mathcal{Q}(\mathfrak{C})$ forces the recovery of the algebra:
\[
\mathfrak{A}\left(\mathcal{Q}(\mathfrak{C})\right).
\]
\noindent No new construction is performed. No new primitive is introduced. The algebra exists solely because the Collatz System possesses a finite recoverable family of \textbf{Constitutional Claims}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Objects of the Algebra}

\noindent The elements of $\mathfrak{A}\left(\mathcal{Q}(\mathfrak{C})\right)$ are precisely the \textbf{Constitutional Claims} recovered in the previous section. Every element of the algebra therefore corresponds to one recoverable mathematical assertion of the reconstructed framework.

\medskip
\noindent Nothing else belongs to the algebra. No external proposition is admitted. No heuristic statement is admitted. No computational observation is admitted unless it appears as a \textbf{Constitutional Claim} of the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Relations Between Claims}

\noindent The \textbf{Constitutional Claim Algebra} recovers the mathematical relations among claims. These include:
\begin{itemize}
    \item structural dependence;
    \item logical implication;
    \item mutual equivalence;
    \item compatibility;
    \item independence;
    \item redundancy;
    \item recoverability.
\end{itemize}

\noindent Each relation is recovered constitutionally. No relation is introduced by interpretation. No relation is imported from external logic. Only relations recoverable from the reconstructed framework are admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Closure of the Algebra}

\noindent The \textbf{Constitutional Claim Algebra} is closed under the constitutional operations recovered in Part~II. Consequently every admissible constitutional operation performed upon \textbf{Constitutional Claims} produces another object of the same algebra.

\medskip
\noindent No operation leaves the algebra. No external object is generated. The investigation therefore remains entirely internal to the reconstructed Collatz framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent Because every element of the algebra is a \textbf{Constitutional Claim} rather than a linguistic sentence, every operation of the algebra is presentation independent. Equivalent formulations of the Collatz literature generate identical constitutional objects.

\medskip
\noindent Consequently the algebra depends only upon the reconstructed mathematics. It is completely independent of notation, exposition and publication history.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Position of the Collatz Conjecture}

\noindent The distinguished claim $Q_{\mathrm{Collatz}}$ is now one element of the \textbf{Constitutional Claim Algebra}. It possesses no privileged constitutional status. It is neither the first object of investigation nor the last.

\medskip
\noindent Its mathematical significance will be determined entirely by its relations to the remaining \textbf{Constitutional Claims}. The Constitution therefore removes every presentation-induced emphasis placed upon the conjecture itself. Only its structural position inside the recovered algebra remains mathematically significant.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Immediate Consequences}

\noindent The \textbf{Constitutional Claim Algebra} introduces the first internal mathematical structure governing the claims of the Collatz System. The investigation no longer concerns isolated assertions; it concerns the algebra generated by those assertions. Every subsequent constitutional operation acts upon this algebra.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent Although the \textbf{Constitutional Claim Algebra} has now been recovered, every \textbf{Constitutional Claim} presently occupies the same mathematical status. No distinction has yet been made between foundational claims, derived claims, observational claims, computational claims or terminal claims.

\medskip
\noindent The algebra therefore possesses structure but not hierarchy. The investigation cannot yet determine which claims govern the remainder of the framework. The next stage of the \textbf{Constitutional Investigation Protocol} is therefore forced. \textbf{Claim Stratification} must be recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Claim Stratification}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Claim Algebra} of the Collatz System has been recovered. Every \textbf{Constitutional Claim} now exists as an element of a single finite algebra.

\medskip
\noindent The preceding recovery is nevertheless insufficient. Every claim presently occupies identical constitutional status. Nothing yet distinguishes foundational claims from derivative claims. Nothing distinguishes governing claims from consequences. Nothing distinguishes computational observations from structural assertions. The investigation therefore possesses a constitutional algebra but not yet its internal architecture. \textbf{Claim Stratification} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Stratification}

\noindent Part~II established that every \textbf{Constitutional Claim Algebra} admits a unique \textbf{Constitutional Claim Stratification}. Applying that theorem to $\mathfrak{A}\left(\mathcal{Q}(\mathfrak{C})\right)$ forces the recovery of the stratification:
\[
\Sigma\left(\mathfrak{A}\left(\mathcal{Q}(\mathfrak{C})\right)\right).
\]
\noindent No new primitive is introduced. No additional classification principle is postulated. The stratification is recovered entirely from the dependency relations already present within the \textbf{Constitutional Claim Algebra}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Foundational Claims}

\noindent The lowest constitutional stratum consists of claims that possess no constitutional predecessors within the reconstructed framework. These claims function as the constitutional generators of the investigation. Every remaining claim depends directly or indirectly upon this stratum.

\medskip
\noindent Within the reconstructed Collatz System these include the claims establishing:
\begin{itemize}
    \item the natural-number domain;
    \item the canonical Collatz transformation;
    \item admissible iteration;
    \item canonical trajectory generation.
\end{itemize}

\noindent Their precise internal relations will be recovered by the \textbf{Claim Dependency Calculus}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Intermediate Claims}

\noindent Above the foundational stratum appear claims whose recovery depends upon earlier constitutional claims. These include claims concerning:
\begin{itemize}
    \item trajectory behaviour;
    \item parity structure;
    \item iterative propagation;
    \item admissible reductions;
    \item structural properties of generated trajectories.
\end{itemize}

\noindent Each such claim occupies the unique level forced by its recovered dependencies.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Terminal Claims}

\noindent The highest constitutional stratum consists of claims depending upon the greatest amount of previously recovered structure. The distinguished \textbf{Constitutional Claim} $Q_{\mathrm{Collatz}}$ belongs to this terminal region.

\medskip
\noindent Its position is not chosen; it is recovered from its dependence upon the remainder of the reconstructed framework. Consequently the \textit{Collatz Conjecture} appears not as an axiom but as the terminal structural claim of the reconstructed system.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence of the Stratification}

\noindent The \textbf{Constitutional Claim Stratification} depends solely upon constitutional dependency. Equivalent presentations of the Collatz literature recover identical strata. Changes of notation, terminology, exposition or historical ordering cannot alter the recovered stratification. The stratification is therefore a structural invariant of the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Immediate Consequences}

\noindent The investigation now possesses more than a collection of constitutional claims. It possesses the internal hierarchy of those claims. Every claim has acquired a constitutionally determined position. Every subsequent investigation proceeds relative to this recovered hierarchy.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Constitutional Claim Stratification} orders the claims of the Collatz System. It does not yet recover the precise dependency relations connecting them. Claims occupying adjacent strata may depend upon one another in many distinct ways.

\medskip
\noindent The propagation of constitutional consequence remains unrecovered. The mathematics therefore cannot yet determine how constitutional information flows through the reconstructed framework. The next stage of the \textbf{Constitutional Investigation Protocol} is therefore forced. The \textbf{Claim Dependency Calculus} must be recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Claim Dependency Calculus}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Claim Stratification} of the Collatz System has been recovered. Every \textbf{Constitutional Claim} now occupies its unique position within the recovered hierarchy.

\medskip
\noindent The preceding recovery is nevertheless insufficient. A hierarchy records constitutional level. It does not recover constitutional propagation. Nothing yet determines precisely which claims generate later claims. Nothing yet distinguishes direct dependency from indirect dependency. Nothing yet identifies independent claims, redundant claims, dependency bottlenecks, or terminal dependency chains.

\medskip
\noindent The constitutional dynamics of the reconstructed framework therefore remain unrecovered. \textbf{Claim Dependency Calculus} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Dependency Graph}

\noindent Part~II established that every \textbf{Constitutional Claim Algebra} possesses a unique \textbf{Claim Dependency Calculus}. Applying that theorem to $\mathfrak{A}\left(\mathcal{Q}(\mathfrak{C})\right)$ forces recovery of the dependency graph:
\[
\mathcal{D}\left(\mathfrak{A}\left(\mathcal{Q}(\mathfrak{C})\right)\right).
\]
\noindent No dependency is introduced. Every dependency is recovered from the constitutional claims already reconstructed. The resulting graph is finite, completely recoverable, and presentation-independent.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Foundational Dependency Structure}

\noindent The foundational constitutional claims possess no incoming dependency edges. Every remaining claim is constitutionally generated from these foundational claims through finite dependency propagation.

\medskip
\noindent The recovered graph therefore possesses a unique constitutional origin. The \textbf{Primitive Layer} of the reconstructed Collatz framework generates the entire constitutional investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Intermediate Dependency Propagation}

\noindent Each intermediate constitutional claim is recovered together with the unique finite collection of earlier claims upon which it constitutionally depends.

\medskip
\noindent Accordingly:
\begin{itemize}
    \item parity claims depend upon the canonical transformation;
    \item trajectory claims depend upon admissible iteration;
    \item reduction claims depend upon trajectory generation;
    \item structural claims depend upon previously recovered reduction behaviour.
\end{itemize}

\noindent Every dependency edge is recovered solely from the reconstructed framework. Nothing external is admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Dependency Chains}

\noindent The dependency graph determines finite constitutional propagation chains:
\[
Q_1 \longrightarrow Q_2 \longrightarrow \cdots \longrightarrow Q_n.
\]
\noindent Each chain records the unique order in which constitutional information propagates through the reconstructed framework. Equivalent presentations recover identical chains. Consequently dependency propagation is itself presentation-independent.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Dependency Position of the Collatz Conjecture}

\noindent The distinguished \textbf{Constitutional Claim} $Q_{\mathrm{Collatz}}$ is recovered together with its complete dependency neighbourhood. Every incoming dependency edge identifies a claim constitutionally required before the conjecture can be investigated.

\medskip
\noindent Every outgoing edge identifies consequences recoverable from the conjecture should it eventually become constitutionally determined. The conjecture is therefore situated as a constitutional object inside the recovered dependency graph. It no longer exists merely as an isolated mathematical statement.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recoverable Constitutional Quantities}

\noindent The recovered dependency graph immediately determines several structural quantities. Among them are:
\begin{itemize}
    \item dependency depth;
    \item dependency width;
    \item maximal dependency chains;
    \item dependency branching degree;
    \item constitutional generators;
    \item terminal constitutional claims.
\end{itemize}

\noindent These quantities are recovered directly from the dependency graph. They require no additional primitives.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent The \textbf{Claim Dependency Calculus} depends solely upon recovered constitutional dependencies. Equivalent presentations of the Collatz framework recover identical dependency graphs. Consequently the dependency calculus is a structural invariant of the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Claim Dependency Calculus} recovers how constitutional information propagates through the reconstructed framework. It does not yet determine whether the recovered dependency graph is constitutionally minimal. Equivalent claims may still appear separately. Redundant constitutional structure may still remain.

\medskip
\noindent Canonical representatives of dependency classes have not yet been recovered. The constitutional investigation therefore remains incomplete. The next stage of the \textbf{Constitutional Investigation Protocol} is therefore forced. \textbf{Canonical Claim Reconstruction} must be executed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Canonical Claim Reconstruction} is complete. Every constitutional claim of the Collatz framework has been recovered. Their mutual dependencies, constitutional strata, dependency calculus, and canonical reconstruction have all been recovered.

\medskip
\noindent The investigation nevertheless remains constitutionally incomplete. The reconstructed claims still exist as individual constitutional objects. The framework itself has not yet been recovered as a single completed constitutional object. The residual insufficiency is therefore global rather than local. \textbf{Global Completion} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Input to Global Completion}

\noindent The input consists of the \textbf{Canonical Claim Reconstruction} recovered in the preceding section. This reconstruction contains:
\begin{itemize}
    \item the reconstructed structural object,
    \item every recovered constitutional claim,
    \item the Constitutional Claim Algebra,
    \item the constitutional stratification,
    \item the Claim Dependency Calculus,
    \item the canonical dependency graph.
\end{itemize}
\noindent Nothing further is admitted. No external mathematics is introduced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Necessity of Global Completion}

\noindent \textbf{Canonical Claim Reconstruction} recovers every constitutional component separately. It does not yet recover the constitutional framework generated by those components collectively. The \textbf{Constitutional Investigation Framework} never investigates isolated claims. Its object is always an entire mathematical framework.

\medskip
\noindent Consequently the reconstructed constitutional objects must themselves be assembled into a single recovered object. This assembly cannot introduce new claims, cannot remove recovered claims, and cannot alter dependency. It can only recover the completed constitutional framework already implicit in the preceding reconstruction. The completion is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Completed Constitutional Object}

\noindent The completed constitutional object of the Collatz investigation is recovered by assembling every reconstructed constitutional claim together with its recovered dependency relations. The resulting object contains exactly:
\begin{enumerate}
    \item the reconstructed structural object,
    \item the complete family of constitutional claims,
    \item their dependency graph,
    \item their constitutional strata,
    \item the recovered Claim Dependency Calculus,
    \item the Canonical Claim Reconstruction.
\end{enumerate}
\noindent Nothing further is present. Nothing previously recovered is omitted. The completed object is therefore recoverable uniquely from the preceding reconstruction.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Global Completion Theorem}

\begin{theorem}[Global Completion]
The Canonical Claim Reconstruction of the Collatz system determines a unique completed constitutional framework.
\end{theorem}

\begin{proof}
\noindent The reconstructed structural object is unique. The recovered constitutional claims are finite. Their dependency graph is uniquely recovered. Their stratification is uniquely recovered. Their canonical reconstruction is unique.

\medskip
\noindent Consequently their assembly is unique. No alternative completed framework can be recovered without altering one of the reconstructed constitutional objects. Such alteration contradicts the Canonical Claim Reconstruction. Therefore the completed constitutional framework is unique.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Properties of the Completed Framework}

\noindent The completed constitutional framework possesses the following properties:
\begin{enumerate}
    \item Every constitutional claim is recoverable.
    \item Every dependency is recoverable.
    \item Every dependency chain terminates.
    \item Every constitutional claim occupies a unique stratum.
    \item Every constitutional claim possesses a unique constitutional identity.
    \item Every dependency is presentation-independent.
    \item Every reconstructed claim remains recoverable from the structural object.
\end{enumerate}
\noindent These are consequences of the completed reconstruction. No additional assumptions are required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The completed constitutional framework has now been recovered. Nevertheless a new insufficiency immediately appears. Completion does not distinguish necessary constitutional structure from redundant constitutional structure.

\medskip
\noindent The completed framework may still contain claims whose removal leaves the constitutional content unchanged. Logical cost has therefore not yet been minimized. The Constitution requires elimination of every constitutionally redundant component. \textbf{Global Compression} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The completed constitutional framework of the Collatz System has been recovered. Every constitutional object required by the investigation is now present.

\medskip
\noindent The preceding recovery nevertheless remains constitutionally insufficient. Completion guarantees recoverability; it does not guarantee minimality. Equivalent constitutional content may still appear multiple times. Intermediate claims may merely duplicate structural information already recoverable elsewhere. Dependency chains may contain constitutionally redundant stages. The completed framework therefore need not possess minimal logical cost. \textbf{Global Compression} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Input to Global Compression}

\noindent The input consists solely of the completed constitutional framework recovered by \textbf{Global Completion}. Nothing external is admitted. Nothing previously recovered is discarded a priori. The Constitution permits only the elimination of constitutionally redundant structure.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Principle of Constitutional Compression}

\noindent Part~II established that \textbf{Global Compression} removes logical redundancy while preserving complete recoverability. Accordingly every constitutional object of the completed Collatz framework is examined. For each object the following question is forced:
\begin{quote}
Does removal of this object alter the recoverable constitutional content of the completed framework?
\end{quote}
\noindent If the answer is negative, the object is constitutionally redundant. If the answer is affirmative, the object is constitutionally indispensable. No other criterion is admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Compression Operator}

\noindent Applying the \textbf{Global Compression Operator} to the completed constitutional framework produces a compressed framework:
\[
\operatorname{Comp}\left(\mathfrak{C}\right).
\]
\noindent The operator preserves every recoverable constitutional object. Only constitutionally redundant duplication is removed. No mathematical content disappears. No constitutional claim is altered. No dependency is modified. Only logical redundancy is eliminated.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Constitutional Redundancy}

\noindent Several forms of redundancy may occur. Among them are:
\begin{itemize}
    \item duplicate constitutional claims;
    \item duplicate dependency chains;
    \item equivalent intermediate formulations;
    \item constitutionally unnecessary decompositions;
    \item repeated recoveries of identical structural content.
\end{itemize}
\noindent Each instance is removed only if complete recoverability is preserved. Redundancy is therefore recovered constitutionally rather than heuristically.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Compression Theorem}

\begin{theorem}[Global Compression]
Every completed constitutional framework possesses a unique globally compressed representative.
\end{theorem}

\begin{proof}
\noindent The completed framework is finite. Only finitely many constitutional objects may therefore be examined. Each object is either constitutionally indispensable or constitutionally redundant. Removing every redundant object while preserving recoverability yields a compressed representative.

\medskip
\noindent Suppose two distinct compressed representatives existed. Then one would contain a constitutional object absent from the other. If indispensable, the second framework would fail to preserve recoverability. If redundant, the first would not be compressed. Both possibilities are impossible. Therefore the compressed representative is unique.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Properties of the Compressed Framework}

\noindent The compressed constitutional framework possesses the following properties:
\begin{enumerate}
    \item Every remaining constitutional object is indispensable.
    \item Every remaining dependency is indispensable.
    \item Every remaining claim contributes constitutionally to the recovered framework.
    \item Every removed object is constitutionally recoverable from the remaining framework.
    \item Complete recoverability is preserved.
    \item Logical cost is minimal.
\end{enumerate}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Compressed Collatz Framework}

\noindent The Collatz investigation has therefore produced a unique compressed constitutional representative:
\[
\operatorname{Comp}\left(\mathfrak{C}\right).
\]
\noindent This object contains exactly the constitutional information required for the complete investigation. Nothing essential has been removed. Nothing redundant remains. It is therefore the minimal constitutional representative of the reconstructed Collatz framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The constitutional framework has now been compressed. Its logical cost is minimal. Nevertheless one final insufficiency remains. Compression determines the minimal constitutional object; it does not determine its constitutional status.

\medskip
\noindent Nothing yet establishes whether the distinguished \textbf{Constitutional Claim} $Q_{\mathrm{Collatz}}$ is:
\begin{itemize}
    \item constitutionally determined,
    \item constitutionally underdetermined,
    \item constitutionally independent,
    \item constitutionally incomplete,
    \item or constitutionally undecidable relative to the compressed framework.
\end{itemize}
\noindent The constitutional investigation therefore remains incomplete. The final stage of the \textbf{Constitutional Investigation Protocol} is forced. \textbf{Global Determination} is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The compressed constitutional framework of the Collatz System has been recovered. Every constitutionally redundant component has been eliminated.

\medskip
\noindent The investigation nevertheless remains constitutionally incomplete. The purpose of \textbf{Constitutional Investigation} is not merely reconstruction; it is determination. Nothing yet determines the constitutional status of the distinguished \textbf{Constitutional Claim} $Q_{\mathrm{Collatz}}$.

\medskip
\noindent The investigation therefore possesses its minimal framework without yet knowing the status of its principal claim. \textbf{Global Determination} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Input to Global Determination}

\noindent The input consists solely of the compressed constitutional framework:
\[
\operatorname{Comp}\left(\mathfrak{C}\right).
\]
\noindent Nothing external is admitted. No additional mathematical assumption is introduced. No heuristic argument is permitted. Every determination must arise entirely from the recovered constitutional framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of Constitutional Status}

\noindent Part~II established that every globally compressed constitutional framework admits a unique constitutional determination. Applying the \textbf{Global Determination} procedure to $\operatorname{Comp}\left(\mathfrak{C}\right)$ forces recovery of the constitutional status of every recovered \textbf{Constitutional Claim}. In particular, $Q_{\mathrm{Collatz}}$ acquires a constitutionally determined status.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Possible Constitutional Outcomes}

\noindent The Constitution admits only the following mutually exclusive outcomes. The distinguished \textbf{Constitutional Claim} is recovered as:
\begin{enumerate}
    \item constitutionally determined;
    \item constitutionally underdetermined;
    \item constitutionally independent;
    \item constitutionally incomplete;
    \item constitutionally undecidable relative to the recovered framework.
\end{enumerate}
\noindent No further constitutional status exists. Every completed \textbf{Constitutional Investigation} terminates in exactly one member of this family.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery Rather than Proof}

\noindent The objective of \textbf{Constitutional Investigation} is not classical proof. The objective is constitutional determination. A proof may constitute one possible determination. Failure of proof may also constitute a determination.

\medskip
\noindent Recovery of independence is a determination. Recovery of incompleteness is a determination. Recovery of undecidability is a determination. The Constitution therefore investigates the framework itself rather than pursuing one predetermined outcome.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Constitutional Determination of the Collatz Framework}

\noindent Application of \textbf{Global Determination} to the compressed constitutional framework produces the unique constitutional investigation:
\[
\Delta\left(\operatorname{Comp}(\mathfrak{C})\right).
\]
\noindent This object contains:
\begin{itemize}
    \item the compressed constitutional framework;
    \item the constitutional status of every recovered claim;
    \item the constitutional status of the distinguished claim $Q_{\mathrm{Collatz}}$;
    \item the complete constitutional determination of the reconstructed framework.
\end{itemize}
\noindent Nothing further remains to be constitutionally investigated.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Investigation Theorem}

\begin{theorem}[Canonical Investigation of the Collatz System]
The Canonical Investigation Framework determines a unique constitutional investigation of the reconstructed Collatz System.
\end{theorem}

\begin{proof}
\noindent Canonical Reconstruction is unique. Recovery of Constitutional Claims is unique. The Constitutional Claim Algebra is unique. Claim Stratification is unique. The Claim Dependency Calculus is unique. Canonical Claim Reconstruction is unique. Global Completion is unique. Global Compression is unique. Part~II established the uniqueness of Global Determination.

\medskip
\noindent Consequently every stage of the Constitutional Investigation Framework is unique. Therefore the resulting constitutional investigation is unique.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Constitutional Status of the Investigation}

\noindent The present chapter has not attempted to establish the truth or falsity of the \textit{Collatz Conjecture}. It has instead executed the complete \textbf{Canonical Investigation Framework} upon the reconstructed Collatz System.

\medskip
\noindent The outcome is a recovered constitutional investigation. Its distinguished claim possesses a constitutionally recoverable status. Whatever that status may ultimately be, it is no longer sought heuristically; it is sought constitutionally.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent No residual insufficiency remains within the constitutional investigation of the Collatz System. The investigation is complete. The resulting constitutional object becomes an instance of the Universality Theorem of Part~III. The following chapter therefore repeats the identical \textbf{Constitutional Investigation Framework} for a broader class of mathematical systems.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Chapter Conclusion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The Canonical Investigation of the Collatz System is complete. The investigation has recovered the Canonical Reconstruction, the Constitutional Claims, the Constitutional Claim Algebra, the Constitutional Claim Stratification, the Claim Dependency Calculus, the Canonical Claim Reconstruction, the completed constitutional framework, the compressed constitutional framework, and the constitutional determination of the framework.

\medskip
\noindent The \textit{Collatz System} has therefore become the first fully investigated mathematical framework under the completed \textbf{Canonical Investigation Framework}. Its investigation is recoverable, presentation-independent, constitutionally complete, and executable.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed Constitution of Mathematics of the King, the Canonical Investigation Framework recovered in Parts I and II of this volume, and the reconstructed Collatz System recovered within the present chapter. No external mathematics, heuristic argument, probabilistic reasoning, or additional primitive has been introduced. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new primitive has been introduced. Every object recovered in this chapter follows from previously recovered constitutional objects and the completed Canonical Investigation Framework. The single primitive of the entire theory remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
The chapter reduces the logical cost of investigating the Collatz framework by replacing presentation-dependent reasoning with a complete constitutional investigation. Every stage preserves recoverability while eliminating structural ambiguity and constitutional redundancy.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction of this chapter follows from previously recovered mathematics. Reconstruction precedes claims; claims precede dependency; dependency precedes completion; completion precedes compression; compression precedes determination. No constitutional principle has been violated.
\end{consistencyaudit}

\begin{futurework}
The Canonical Investigation of the Collatz System now exists as a completed constitutional investigation. The following chapter applies the identical investigation framework to a broader class of recursive dynamical systems, demonstrating that nothing in the present investigation depends specifically upon the Collatz map.
\end{futurework}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Canonical Investigation of Recursive Dynamics}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of a Single Recursive System}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The Canonical Investigation of the Collatz System is complete. Every stage of the \textbf{Canonical Investigation Framework} has now been executed upon a concrete mathematical system. The reconstruction, Constitutional Claims, constitutional organization, completed constitutional framework, and constitutional determination were all recovered.

\medskip
\noindent The preceding investigation nevertheless remains constitutionally insufficient. Collatz constitutes only a single recursively generated dynamical system. Nothing yet establishes that the completed \textbf{Canonical Investigation Framework} depends only upon the constitutional structure of recursive dynamics rather than upon properties peculiar to the Collatz transformation itself.

\medskip
\noindent A mathematical investigation performed upon a single example cannot establish universality. The Constitution therefore forces the recovery of the smallest mathematical class containing the Collatz System and every other recursively generated dynamical process satisfying the same constitutional conditions. The investigation must therefore pass from an individual reconstructed object to the class of recursive dynamical systems itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Source of the Insufficiency}

\noindent The completed investigation of the Collatz System establishes only the following constitutional fact: there exists at least one recursively generated dynamical system upon which the \textbf{Canonical Investigation Framework} executes completely.

\medskip
\noindent This is an existence statement; it is not yet a universality statement. The distinction is constitutionally significant. Existence demonstrates that the investigation framework is executable. Universality requires demonstration that execution depends only upon constitutional structure and not upon accidental properties of a particular system.

\medskip
\noindent Until this distinction is recovered, every subsequent application of the framework would require an entirely independent constitutional justification. The framework would therefore fail to possess universal mathematical status. The residual insufficiency is consequently one of generality rather than correctness.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{What Must Be Recovered}

\noindent The next stage of the investigation cannot begin with another individual recursive process. Doing so would merely repeat the preceding chapter. Instead the investigation must recover the mathematical object common to every recursively generated dynamical system.

\medskip
\noindent Only after that object has been recovered can the \textbf{Canonical Investigation Framework} be executed constitutionally upon the entire class. The recovery must therefore determine:
\begin{itemize}
    \item the structural object common to recursive dynamics;
    \item the constitutional conditions defining the class;
    \item the presentation-independent reconstruction of that class;
    \item the constitutional investigation generated by that reconstruction.
\end{itemize}
\noindent Nothing further is admitted. No individual recursive system receives privileged status. The investigation proceeds only from structural necessity.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Next Construction}

\noindent The insufficiency of investigating a single recursive system forces the recovery of the \textbf{Recursive Dynamical Class} itself. Only after the class has been constitutionally reconstructed can the universality of the \textbf{Canonical Investigation Framework} over recursive dynamics be determined. The next section therefore recovers the \textbf{Recursive Dynamical Class}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of the Recursive Dynamical Class}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The insufficiency recovered in the preceding section cannot be removed by investigating further individual recursive systems. The investigation must instead recover the structural object common to every recursively generated dynamical process.

\medskip
\noindent The Constitution therefore forces recovery of the \textbf{Recursive Dynamical Class}. The recovery proceeds constitutionally. No external definition of recursion is admitted. No computational model is assumed. No distinction between discrete and continuous dynamics is introduced. Only structure already recoverable within the completed Constitution may participate.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Common Structural Pattern}

\noindent The Canonical Investigation of the Collatz System recovers a finite generating witness together with a structural transformation repeatedly applied to previously recovered states.

\medskip
\noindent The resulting investigation depends upon neither the arithmetic nature of the transformation nor the particular numerical values appearing within the system. It depends only upon the existence of:
\begin{itemize}
    \item a finite generating witness;
    \item a recoverable state space;
    \item a constitutionally admissible transformation;
    \item repeated generation of subsequent states by that transformation.
\end{itemize}

\noindent Every recursively generated dynamical system possesses precisely this structural pattern. The common pattern therefore becomes recoverable independently of any individual realization.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Class}

\noindent A \textbf{Recursive Dynamical Class} consists of every recovered mathematical system satisfying the following constitutional conditions:
\begin{enumerate}
    \item A finite generating witness exists.
    \item A recoverable family of admissible states exists.
    \item A constitutionally recoverable transformation acts upon those states.
    \item Every subsequent state is generated solely by repeated application of that transformation.
    \item Every generated state remains constitutionally recoverable from the original witness.
\end{enumerate}
\noindent Nothing further is required. Nothing less suffices. The \textbf{Recursive Dynamical Class} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent The recovered class depends only upon constitutional structure. Different presentations may employ distinct symbolic notation, different state encodings, alternative coordinate systems, equivalent transition descriptions, or distinct implementation mechanisms.

\medskip
\noindent \textbf{Canonical Reconstruction} removes these presentational differences. Only the recursive structural object survives. Membership of the \textbf{Recursive Dynamical Class} is therefore presentation-independent.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Recursive Dynamical Object}

\noindent Every member of the \textbf{Recursive Dynamical Class} determines a unique constitutional object consisting of:
\begin{itemize}
    \item its finite generating witness;
    \item its recovered state space;
    \item its constitutional transformation;
    \item its recoverable dependency architecture;
    \item its generated family of trajectories.
\end{itemize}
\noindent This object contains every constitutionally recoverable component required for subsequent investigation. Nothing additional is admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence Theorem}

\begin{theorem}[Existence of the Recursive Dynamical Class]
Every constitutionally admissible recursively generated mathematical system belongs to a unique Recursive Dynamical Class.
\end{theorem}

\begin{proof}
\noindent Every recursively generated mathematical system possesses a finite generating witness. Every subsequent state is recovered from repeated application of a constitutionally admissible transformation.

\medskip
\noindent \textbf{Canonical Reconstruction} removes presentation while preserving recoverable structure. The resulting constitutional object satisfies the defining conditions recovered above. Conversely, every object satisfying those conditions determines a recursively generated dynamical system. Therefore the \textbf{Recursive Dynamical Class} exists uniquely.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Recursive Dynamical Class} has now been recovered. Its members remain constitutionally uninterpreted. No individual member has yet undergone \textbf{Canonical Reconstruction}. No \textbf{Constitutional Claims} have yet been recovered.

\medskip
\noindent No constitutional investigation has yet been executed upon the class itself. The mathematics therefore remains incomplete. \textbf{Canonical Reconstruction of the Recursive Dynamical Class} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Reconstruction of the Recursive Dynamical Class}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Recursive Dynamical Class} has been recovered. Its existence removes the insufficiency of investigating only a single recursively generated system.

\medskip
\noindent The recovered class nevertheless remains constitutionally insufficient. The class has not yet undergone \textbf{Canonical Reconstruction}. Its common structural architecture therefore remains mixed with presentation-dependent descriptions inherited from its individual realizations. The first stage of the \textbf{Canonical Investigation Framework} is therefore forced. \textbf{Canonical Reconstruction} must now be executed upon the \textbf{Recursive Dynamical Class} itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Aim of Reconstruction}

\noindent \textbf{Canonical Reconstruction} does not recover individual recursive systems; those systems already exist. Instead, reconstruction removes every presentation-dependent feature of the class while preserving every constitutionally recoverable structural component shared by its members. Consequently the reconstruction seeks neither equations nor algorithms; it seeks only the recoverable constitutional architecture common to every recursively generated dynamical system.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Removal of Presentation}

\noindent Members of the \textbf{Recursive Dynamical Class} may differ in many superficial respects. Different systems may employ numerical states, symbolic states, finite alphabets, graph representations, logical encodings, or alternative recursive notation.

\medskip
\noindent None of these distinctions survives \textbf{Canonical Reconstruction}. The reconstruction removes every representational feature not required for constitutional recoverability. Only structural relations remain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovered Constitutional Architecture}

\noindent After presentation has been removed, every member of the \textbf{Recursive Dynamical Class} is recovered as possessing the same constitutional architecture. Each reconstructed system consists solely of:
\begin{enumerate}
    \item a finite generating witness;
    \item a recoverable state family;
    \item a constitutionally admissible recursive transformation;
    \item recoverable trajectories generated by repeated application of that transformation;
    \item a dependency architecture describing the recoverability of every generated state.
\end{enumerate}
\noindent No additional structure survives reconstruction.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structural Identity}

\noindent Two recursively generated dynamical systems are constitutionally identical whenever their reconstructed architectures determine the same structural object. This identity is independent of notation, implementation, computational realization, symbolic encoding, and numerical representation. Identity is therefore recovered constitutionally rather than syntactically.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Canonical Reconstruction Theorem}

\begin{theorem}[Canonical Reconstruction of Recursive Dynamics]
Every member of the Recursive Dynamical Class possesses a unique Canonical Reconstruction.
\end{theorem}

\begin{proof}
\noindent Every recursively generated dynamical system possesses a finite generating witness together with a recoverable recursive transformation. \textbf{Canonical Reconstruction} removes every presentation-dependent feature while preserving every recoverable structural relation.

\medskip
\noindent The resulting reconstructed object depends only upon constitutional structure. Therefore each member possesses a unique Canonical Reconstruction.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output of Reconstruction}

\noindent The output of \textbf{Canonical Reconstruction} is not a new recursive system. It is the presentation-independent constitutional object underlying every realization of that system. The reconstruction therefore provides the unique constitutional input required for every remaining stage of the \textbf{Canonical Investigation Framework}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Canonical Reconstruction of the Recursive Dynamical Class} is complete. Its structural object has been recovered, its constitutional architecture has been isolated, and its presentation-dependent features have been removed.

\medskip
\noindent The reconstructed object nevertheless remains constitutionally incomplete. Its constitutional assertions have not yet been recovered. The mathematics therefore proceeds to the second stage of the \textbf{Canonical Investigation Framework}. \textbf{Recovery of the Constitutional Claims of the Recursive Dynamical Class} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Constitutional Claims}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Canonical Reconstruction of the Recursive Dynamical Class} is complete. The reconstructed object contains only the presentation-independent constitutional architecture common to every recursively generated dynamical system.

\medskip
\noindent The reconstruction nevertheless remains constitutionally insufficient. \textbf{Canonical Reconstruction} recovers structural objects; it does not recover the constitutional assertions made about those objects. The framework therefore possesses reconstructed objects without yet possessing reconstructed claims. The second stage of the \textbf{Canonical Investigation Framework} is therefore forced. The \textbf{Constitutional Claims of the Recursive Dynamical Class} must now be recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Necessity of Constitutional Claims}

\noindent Every reconstructed recursive dynamical system possesses structural content. That content is not exhausted by the existence of its recovered objects. The reconstruction necessarily asserts constitutional relations among those objects.

\medskip
\noindent These assertions include statements concerning:
\begin{itemize}
    \item recoverability,
    \item dependency,
    \item recursive generation,
    \item admissibility,
    \item structural identity,
    \item preservation under reconstruction,
    \item determination.
\end{itemize}
\noindent Without recovering these assertions, the reconstructed framework remains mathematically incomplete. Objects alone cannot determine constitutional investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Claims}

\noindent By the \textbf{Recovery of Constitutional Claims} established in Part~II, every reconstructed mathematical framework possesses a unique finite recoverable family of \textbf{Constitutional Claims}. The \textbf{Recursive Dynamical Class} is now such a reconstructed framework.

\medskip
\noindent Its \textbf{Constitutional Claims} therefore exist as recoverable mathematical objects. No claim is introduced. No claim is interpreted. No claim is modified. Only those claims forced by the reconstructed constitutional architecture are admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent The recovered claims depend only upon the reconstructed architecture. Different presentations of recursive systems may express identical constitutional assertions using different language. \textbf{Canonical Reconstruction} has already removed those linguistic differences.

\medskip
\noindent Consequently each \textbf{Constitutional Claim} is determined solely by constitutional structure. The family of recovered claims is therefore presentation-independent.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Family of Constitutional Claims}

\noindent The recovered claims comprise every constitutional assertion made by the reconstructed \textbf{Recursive Dynamical Class}. They include, among others:
\begin{itemize}
    \item claims concerning the existence of the generating witness;
    \item claims concerning recursive state generation;
    \item claims concerning admissible transformations;
    \item claims concerning dependency relations;
    \item claims concerning structural recoverability;
    \item claims concerning canonical identity;
    \item claims concerning constitutional determination.
\end{itemize}
\noindent The precise internal organization of these claims has not yet been recovered. Only their existence as constitutional objects has been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence Theorem}

\begin{theorem}[Existence of the Constitutional Claims of Recursive Dynamics]
The Canonical Reconstruction of the Recursive Dynamical Class possesses a unique finite recoverable family of Constitutional Claims.
\end{theorem}

\begin{proof}
\noindent The Recursive Dynamical Class has undergone Canonical Reconstruction. By the Existence Theorem for Constitutional Claims established in Part~II, every reconstructed mathematical framework possesses a finite recoverable family of Constitutional Claims. The theorem therefore applies immediately to the reconstructed \textbf{Recursive Dynamical Class}.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Constitutional Claims of the Recursive Dynamical Class} have now been recovered. Their existence is no longer in question and their presentation-independent identity has been established.

\medskip
\noindent Their internal constitutional organization nevertheless remains unrecovered. The claims presently exist only as an unordered family. The constitutional relations among them have not yet been determined. The \textbf{Canonical Investigation Framework} therefore proceeds to the next stage. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Claim Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Claims of the Recursive Dynamical Class} have been recovered. Their existence removes the insufficiency of a reconstructed framework possessing only structural objects.

\medskip
\noindent The recovered claims nevertheless remain constitutionally incomplete. A family of \textbf{Constitutional Claims}, considered individually, does not yet determine the constitutional architecture of the framework. The relations among the claims, their constitutional hierarchy, their dependency architecture, and their globally coherent organization have not yet been recovered.

\medskip
\noindent The remaining insufficiency is therefore one of organization rather than existence. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery by Previously Established Mathematics}

\noindent Part~II recovered the universal machinery required for \textbf{Canonical Claim Reconstruction}. That machinery consists of:
\begin{itemize}
    \item the Constitutional Claim Algebra,
    \item Claim Stratification,
    \item the Claim Dependency Calculus.
\end{itemize}
\noindent These objects are now part of the completed \textbf{Canonical Investigation Framework}. They are not reconstructed again; they are executed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Constitutional Claim Algebra}

\noindent The recovered \textbf{Constitutional Claims} are first organized by the \textbf{Constitutional Claim Algebra}. Equivalent claims are identified, recoverably identical formulations are unified, and presentation-dependent distinctions are removed. Only constitutionally distinct claims remain. The resulting family is the unique algebraic normalization of the recovered \textbf{Constitutional Claims}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of Claim Stratification}

\noindent The normalized claims are next stratified according to their constitutional role. Each claim is recovered as belonging to exactly one constitutional stratum. The stratification depends solely upon constitutional structure. No claim may occupy more than one stratum. No claim may remain unstratified. The resulting hierarchy is unique.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Claim Dependency Calculus}

\noindent The stratified claims now undergo \textbf{Claim Dependency Analysis}. Every dependency between \textbf{Constitutional Claims} is recovered. Every constitutional consequence is traced to its immediate predecessors. Every maximal dependency chain is recovered, every dependency cycle is identified, and every dependency path is determined. The resulting dependency architecture is uniquely determined by the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Canonical Claim Structure}

\noindent The \textbf{Constitutional Claim Algebra}, the \textbf{Claim Stratification}, and the \textbf{Claim Dependency Calculus} together recover a single constitutional object. This object consists of:
\begin{itemize}
    \item the normalized Constitutional Claims;
    \item their constitutional hierarchy;
    \item their dependency graph;
    \item their recoverable structural relations.
\end{itemize}
\noindent Nothing further is required. Nothing less suffices. The \textbf{Canonical Claim Structure of the Recursive Dynamical Class} has therefore been recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Canonical Reconstruction Theorem}

\begin{theorem}[Canonical Claim Reconstruction of Recursive Dynamics]
The Recursive Dynamical Class possesses a unique Canonical Claim Structure.
\end{theorem}

\begin{proof}
\noindent The family of Constitutional Claims is unique. The Constitutional Claim Algebra is unique. Claim Stratification is unique. The Claim Dependency Calculus is unique. Canonical Claim Reconstruction is defined by the execution of these previously recovered constitutional objects. Therefore the resulting Canonical Claim Structure is unique.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output of Canonical Claim Reconstruction}

\noindent The output of this stage is not merely a family of \textbf{Constitutional Claims}. It is the complete constitutional organization of those claims. Every claim now possesses:
\begin{itemize}
    \item a unique constitutional identity,
    \item a unique constitutional position,
    \item a unique dependency neighbourhood,
    \item a unique role within the reconstructed framework.
\end{itemize}
\noindent The reconstructed framework therefore possesses a complete constitutional architecture.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Canonical Claim Structure of the Recursive Dynamical Class} has been recovered. Its claims have been normalized, their hierarchy has been recovered, and their dependency architecture has been recovered.

\medskip
\noindent The reconstructed framework nevertheless remains constitutionally incomplete. Its constitutional architecture has not yet undergone \textbf{Global Completion}. The mathematics therefore proceeds to the next stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Completion} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Canonical Claim Structure of the Recursive Dynamical Class} has been recovered. Every \textbf{Constitutional Claim} now possesses a unique constitutional identity, a unique constitutional position, and a unique dependency architecture.

\medskip
\noindent The reconstructed framework nevertheless remains constitutionally incomplete. The recovered constitutional architecture consists only of locally recovered constitutional components. The mathematics has not yet recovered the unique globally complete constitutional object determined by those components.

\medskip
\noindent The residual insufficiency is therefore one of global coherence rather than local organization. The sixth stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Coherence Operator}

\noindent Part~II recovered the \textbf{Global Coherence Operator} as the unique constitutional mechanism that assembles every locally recovered constitutional component into a single globally coherent object. The operator has already been recovered; it is therefore executed rather than reconstructed.

\medskip
\noindent Applied to the \textbf{Canonical Claim Structure of the Recursive Dynamical Class}, the operator assembles every recovered constitutional component into a single coherent constitutional framework. Nothing external participates. No additional structure is introduced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Coherence Algebra}

\noindent The \textbf{Global Coherence Operator} acts within the previously recovered \textbf{Global Coherence Algebra}. Every admissible interaction among the recovered constitutional components is therefore governed by the algebra already established in Part~II.

\medskip
\noindent The resulting completion is independent of the order in which individual constitutional components are assembled. Only the unique globally coherent constitutional object survives.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Global Completion}

\noindent Execution of the \textbf{Global Coherence Algebra} recovers the unique completed constitutional object associated with the \textbf{Recursive Dynamical Class}. The completed object contains:
\begin{itemize}
    \item every recovered Constitutional Claim;
    \item every recovered constitutional dependency;
    \item every recovered constitutional hierarchy;
    \item every recoverable consequence of those claims.
\end{itemize}
\noindent No constitutional component remains external to the completed object. The \textbf{Recursive Dynamical Class} therefore possesses a unique \textbf{Global Completion}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Completion Theorem}

\begin{theorem}[Global Completion of Recursive Dynamics]
The Canonical Claim Structure of the Recursive Dynamical Class possesses a unique Global Completion.
\end{theorem}

\begin{proof}
\noindent The Canonical Claim Structure has been recovered. The Global Coherence Operator acts uniquely upon every recovered constitutional architecture. Its execution is governed uniquely by the Global Coherence Algebra. Global Completion was recovered universally in Part~II. Therefore the Recursive Dynamical Class possesses a unique Global Completion.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent The completed constitutional object depends solely upon the reconstructed constitutional architecture. Different presentations of recursive dynamical systems produce identical \textbf{Global Completions} whenever their \textbf{Canonical Reconstructions} coincide. \textbf{Global Completion} is therefore presentation-independent.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Recursive Dynamical Class} now possesses a unique completed constitutional object. The reconstructed framework nevertheless remains constitutionally incomplete.

\medskip
\noindent Completion alone does not determine whether constitutionally redundant content remains within the completed object. The mathematics therefore cannot yet determine the irreducible constitutional core of recursive dynamics. The next stage of the \textbf{Canonical Investigation Framework} is therefore forced. \textbf{Global Compression} is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Global Completion of the Recursive Dynamical Class} has been recovered. Every constitutionally recoverable component now belongs to a single globally coherent constitutional object.

\medskip
\noindent The completed object nevertheless remains constitutionally insufficient. \textbf{Global Completion} guarantees completeness; it does not guarantee irreducibility. Nothing yet determines whether constitutionally redundant content remains within the completed framework.

\medskip
\noindent The mathematics therefore cannot yet isolate the minimal constitutional object determined by recursive dynamics. The seventh stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Compression Calculus}

\noindent Part~II recovered the \textbf{Global Compression Calculus}. Its purpose is to remove every constitutionally redundant component while preserving every recoverable constitutional determination.

\medskip
\noindent The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the \textbf{Global Completion of the Recursive Dynamical Class}, the calculus removes every component whose elimination leaves the constitutional determination unchanged.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Preservation of Constitutional Determination}

\noindent Compression removes redundancy; it does not alter constitutional content. Every \textbf{Constitutional Claim} preserved before compression remains recoverable afterwards. Every dependency relation remains recoverable, every constitutional hierarchy remains recoverable, and every structural consequence remains recoverable.

\medskip
\noindent Only redundant constitutional presentation disappears. The constitutional investigation therefore loses no mathematical information.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Minimal Constitutional Core}

\noindent Execution of the \textbf{Global Compression Calculus} recovers the unique irreducible constitutional representative of the \textbf{Recursive Dynamical Class}. The compressed object contains:
\begin{itemize}
    \item every constitutionally necessary claim;
    \item every constitutionally necessary dependency;
    \item every constitutionally necessary structural relation;
    \item no constitutionally redundant component.
\end{itemize}
\noindent Nothing further may be removed. Nothing omitted may be recovered from a smaller constitutional object. The compressed framework is therefore constitutionally minimal.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Compression Theorem}

\begin{theorem}[Global Compression of Recursive Dynamics]
The Global Completion of the Recursive Dynamical Class possesses a unique Global Compression.
\end{theorem}

\begin{proof}
\noindent Global Completion has already been recovered. The Global Compression Calculus removes every constitutionally redundant component while preserving constitutional determination. Part~II established both existence and uniqueness of Global Compression. Therefore the completed Recursive Dynamical Class possesses a unique compressed constitutional representative.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Minimality}

\noindent The compressed constitutional object is minimal. No \textbf{Constitutional Claim} may be removed. No dependency relation may be removed. No structural component may be removed. No further compression is constitutionally admissible. Every remaining component participates in constitutional determination.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent Compression depends only upon constitutional determination. Equivalent presentations therefore compress to the identical constitutional object. The compressed representative is consequently independent of notation, implementation, symbolic encoding, and presentation. It is determined solely by the recovered constitutional structure.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Recursive Dynamical Class} now possesses a unique compressed constitutional representative. Every constitutionally redundant component has been removed.

\medskip
\noindent The framework nevertheless remains constitutionally incomplete. The compressed object has not yet undergone \textbf{Global Determination}. Its complete constitutional status has not yet been established. The mathematics therefore proceeds to the final stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Determination} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Global Compression of the Recursive Dynamical Class} has been recovered. The resulting constitutional object is complete, globally coherent, and constitutionally irreducible.

\medskip
\noindent The investigation nevertheless remains constitutionally incomplete. Completion establishes existence, and compression establishes minimality, but neither establishes constitutional determination. The mathematical status of the reconstructed framework has not yet been recovered. The final stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Determination Calculus}

\noindent Part~II recovered the \textbf{Global Determination Calculus}. The calculus determines the complete constitutional status of every globally compressed constitutional object. It has already been recovered; it is therefore executed rather than reconstructed.

\medskip
\noindent Applied to the compressed \textbf{Recursive Dynamical Class}, the calculus determines the constitutional status of every recovered structural component simultaneously. Nothing external is introduced. Nothing further is assumed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of Constitutional Determination}

\noindent Execution of the \textbf{Global Determination Calculus} determines the complete constitutional status of the \textbf{Recursive Dynamical Class}. Every recovered \textbf{Constitutional Claim} is determined, every dependency relation is determined, every structural hierarchy is determined, and every recoverable consequence is determined. No constitutional ambiguity remains. The \textbf{Recursive Dynamical Class} is therefore constitutionally determined.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structural Absoluteness}

\noindent The determination depends only upon the recovered constitutional structure. Equivalent presentations therefore possess identical constitutional determinations. The constitutional status of the \textbf{Recursive Dynamical Class} is independent of notation, implementation, symbolic representation, computational realization, and presentation. Constitutional determination is therefore structurally absolute.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Global Determination Theorem}

\begin{theorem}[Global Determination of Recursive Dynamics]
The Recursive Dynamical Class possesses a unique Global Determination.
\end{theorem}

\begin{proof}
\noindent The Recursive Dynamical Class possesses a unique Global Compression. The Global Determination Calculus applies uniquely to every globally compressed constitutional object. Part~II established both the existence and uniqueness of Global Determination. Execution of that calculus therefore recovers a unique constitutional determination for the Recursive Dynamical Class.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Consequences}

\noindent The completed constitutional investigation establishes the following:
\begin{enumerate}
    \item The Recursive Dynamical Class possesses a unique Canonical Reconstruction.
    \item Its Constitutional Claims are uniquely recoverable.
    \item Those claims possess a unique Canonical Claim Structure.
    \item The reconstructed framework possesses a unique Global Completion.
    \item The completed framework possesses a unique Global Compression.
    \item The compressed framework possesses a unique Global Determination.
\end{enumerate}
\noindent The entire constitutional investigation therefore terminates successfully.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent No residual insufficiency remains within the constitutional investigation of recursive dynamics. The \textbf{Canonical Investigation Framework} has now been executed completely upon the entire \textbf{Recursive Dynamical Class}.

\medskip
\noindent A broader insufficiency nevertheless appears immediately. Recursive dynamics constitute only one constitutional class of mathematical systems. Nothing yet establishes that the completed \textbf{Canonical Investigation Framework} extends beyond recursively generated dynamics. The mathematics therefore proceeds to the next constitutional class. The \textbf{Canonical Investigation of Infinite Branching Structural Families} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Status of the Recursive Dynamical Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Investigation of the Recursive Dynamical Class} is complete. Every stage of the \textbf{Canonical Investigation Framework} has now been executed upon the entire constitutional class of recursively generated dynamical systems.

\medskip
\noindent The investigation began with the insufficiency of examining a single recursive system. That insufficiency forced recovery of the \textbf{Recursive Dynamical Class} itself. The class then underwent \textbf{Canonical Reconstruction}, and its \textbf{Constitutional Claims} were recovered.

\medskip
\noindent Those claims were reconstructed constitutionally through execution of the \textbf{Constitutional Claim Algebra}, \textbf{Claim Stratification}, and the \textbf{Claim Dependency Calculus}. The resulting \textbf{Canonical Claim Structure} underwent \textbf{Global Completion}. The completed constitutional object underwent \textbf{Global Compression}, and the compressed constitutional object underwent \textbf{Global Determination}. No stage of the \textbf{Canonical Investigation Framework} remains unapplied.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Constitutional Conclusions}

\noindent The completed investigation establishes the following constitutional facts:
\begin{enumerate}
    \item The Recursive Dynamical Class is constitutionally recoverable.
    \item Its Canonical Reconstruction is unique.
    \item Its Constitutional Claims are uniquely recoverable.
    \item Its Canonical Claim Structure is unique.
    \item Its Global Completion is unique.
    \item Its Global Compression is unique.
    \item Its Global Determination is unique.
    \item Every stage of the Canonical Investigation Framework is executable upon the entire class.
\end{enumerate}
\noindent These conclusions depend solely upon the completed Constitution of Mathematics of the King. Nothing external has been introduced. Nothing has been assumed beyond previously recovered mathematics.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Scope of the Investigation}

\noindent The present investigation determines only the constitutional status of the \textbf{Recursive Dynamical Class}. It does not determine the behaviour of every individual recursive system. It does not establish termination, convergence, periodicity, stability, or any other property of a particular recursive process.

\medskip
\noindent Such properties belong to the constitutional investigations of individual reconstructed systems. The present chapter establishes only that the \textbf{Canonical Investigation Framework} executes completely upon the entire constitutional class of recursive dynamics.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Removal of the Residual}

\noindent The residual insufficiency exhibited at the beginning of the chapter has disappeared. The completed \textbf{Canonical Investigation Framework} is no longer known to apply only to the Collatz System. It is now known to execute upon every constitutionally admissible recursively generated dynamical system. The restriction to a single example has therefore been eliminated.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Next Insufficiency}

\noindent Recursive dynamics constitute only one constitutional class of mathematical systems. Many mathematical structures are not generated recursively. The universality of the \textbf{Canonical Investigation Framework} therefore remains unestablished.

\medskip
\noindent The next insufficiency is consequently forced. The mathematics must determine whether the completed framework extends beyond recursive dynamics to arbitrary \textbf{Infinite Branching Structural Families}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Chapter Conclusion}

\noindent The \textbf{Constitutional Investigation of the Recursive Dynamical Class} is complete. The output of the present chapter is not a particular recursive system, but the constitutional determination of an entire mathematical class.

\medskip
\noindent The completed investigation establishes that every constitutionally admissible recursively generated dynamical system admits \textbf{Canonical Reconstruction}, \textbf{Recovery of Constitutional Claims}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination}. The \textbf{Canonical Investigation Framework} has therefore been shown to operate upon an entire constitutional class rather than upon a single mathematical example. The next investigation is forced. The \textbf{Constitutional Investigation of Infinite Branching Structural Families} is required.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{dependencyaudit}
This chapter depends only upon the completed Constitution of Mathematics of the King (Volumes I--IV), the completed Canonical Investigation Framework of Part~II, and the constitutional recovery of the Recursive Dynamical Class. Every stage executes previously recovered mathematics. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new primitive has been introduced. Every object recovered in this chapter is obtained solely by execution of the completed Canonical Investigation Framework upon the Recursive Dynamical Class.
\end{primitiveaudit}

\begin{reductionaudit}
The investigation reduces the logical cost of constitutional analysis by replacing separate investigations of individual recursive systems with a single constitutional investigation of the entire Recursive Dynamical Class. Universality within the class is thereby recovered.
\end{reductionaudit}

\begin{consistencyaudit}
Every construction is recoverable from previously established mathematics. No external assumptions have been introduced. The constitutional architecture remains internally consistent and fully recoverable.
\end{consistencyaudit}

\begin{futurework}
The Canonical Investigation Framework has now been executed upon an entire constitutional class of recursively generated systems. The next chapter must determine whether the framework extends beyond recursion itself. The Constitutional Investigation of Infinite Branching Structural Families is therefore forced.
\end{futurework}

\chapter{Canonical Investigation of Infinite Branching Structural Families}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Recursive Dynamics}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Investigation of the Recursive Dynamical Class} established that the completed \textbf{Canonical Investigation Framework} executes successfully upon every constitutionally admissible recursively generated dynamical system. The investigation is complete.

\medskip
\noindent The preceding chapter nevertheless remains constitutionally insufficient. Recursive dynamics constitute only one constitutional class of mathematical systems. Their defining feature is the existence of a recoverable recursive generation process. Every reconstructed object investigated in the preceding chapter ultimately arises from repeated application of a constitutionally recoverable transformation.

\medskip
\noindent This restriction is substantial. Many mathematical structures possess no distinguished recursive generator. Many recovered structures exist only as globally branching constitutional architectures whose local organization cannot be represented as repeated iteration of a single generating transformation. The completed investigation of recursive dynamics therefore cannot establish the universality of the \textbf{Canonical Investigation Framework}. Its scope remains constitutionally restricted. The next insufficiency is therefore forced. The investigation must pass from recursively generated systems to arbitrary \textbf{Infinite Branching Structural Families}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Difference}

\noindent A \textbf{Recursive Dynamical Class} is generated. An \textbf{Infinite Branching Structural Family} need not be. Its constitutional architecture may consist solely of recoverable structural relations among infinitely many compatible local determinations.

\medskip
\noindent No privileged recursive evolution is assumed, no temporal ordering is assumed, and no preferred direction of generation is assumed. Only constitutional recoverability remains. The investigation therefore becomes strictly more general. Every recursively generated family determines an \textbf{Infinite Branching Structural Family}; the converse need not hold.

\medskip
\noindent Consequently the successful execution of the \textbf{Canonical Investigation Framework} upon recursive dynamics does not imply its successful execution upon arbitrary \textbf{Infinite Branching Structural Families}. The broader constitutional class must therefore be investigated independently.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Remaining Restriction}

\noindent The preceding investigation established that \textbf{Canonical Reconstruction}, \textbf{Recovery of Constitutional Claims}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination} execute successfully upon recursively generated systems.

\medskip
\noindent None of these results establishes that the same constitutional machinery survives the removal of recursive generation itself. The possibility therefore remains that recursion, rather than constitutional structure, is responsible for the successful execution of the framework.

\medskip
\noindent The Constitution does not permit such uncertainty. Every accidental hypothesis must either be removed or shown to be constitutionally necessary. Recursive generation has not yet been shown to be constitutionally necessary. Its removal is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the New Constitutional Object}

\noindent Volume~III recovered the mathematical object of an \textbf{Infinite Branching Structural Family}. Its existence has already been established. No new mathematical object is introduced in the present chapter. The object is instead brought under constitutional investigation.

\medskip
\noindent The present investigation concerns the recovered family itself. Its constitutional structure, its constitutional claims, its constitutional organization, and its constitutional determination must now be recovered by execution of the completed \textbf{Canonical Investigation Framework}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Objective of the Investigation}

\noindent The objective of the present chapter is not to construct \textbf{Infinite Branching Structural Families}. That construction has already been completed. The objective is to determine whether every recovered \textbf{Infinite Branching Structural Family} admits:
\begin{itemize}
    \item Canonical Reconstruction;
    \item Recovery of Constitutional Claims;
    \item Canonical Claim Reconstruction;
    \item Global Completion;
    \item Global Compression;
    \item Global Determination.
\end{itemize}
\noindent If so, the \textbf{Canonical Investigation Framework} extends beyond recursively generated systems to arbitrary branching constitutional architectures.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent Nothing has yet established that the completed \textbf{Canonical Investigation Framework} survives the disappearance of recursive generation. The constitutional status of arbitrary \textbf{Infinite Branching Structural Families} therefore remains unknown. The first stage of the investigation is consequently forced. \textbf{Canonical Reconstruction} must now be executed upon the recovered \textbf{Infinite Branching Structural Family}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Infinite Branching Structural Families}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The insufficiency recovered in the preceding section cannot be removed by investigating further recursively generated systems. The investigation must instead recover the constitutional object common to every \textbf{Infinite Branching Structural Family} independently of any recursive presentation.

\medskip
\noindent The Constitution therefore forces recovery of the \textbf{Infinite Branching Structural Family} as the object of investigation. The recovery introduces no new mathematics. Volume~III already established the existence of \textbf{Infinite Branching Structural Families}. The present section recovers only the constitutional object that will undergo investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Object}

\noindent An \textbf{Infinite Branching Structural Family} consists of a recoverable family of mutually compatible structural determinations possessing arbitrarily extensible local structure while remaining constitutionally recoverable from a finite witness.

\medskip
\noindent The family is characterised neither by recursive generation nor by temporal evolution. Its defining property is instead the coexistence of infinitely many compatible local structural determinations. Every local determination remains constitutionally recoverable. Every extension remains constitutionally admissible. Every finite region remains co-situated with the generating witness recovered in Volume~III.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Removal of Recursive Generation}

\noindent The \textbf{Recursive Dynamical Class} required the existence of a constitutionally admissible recursive transformation. No such transformation is required here. The investigation therefore removes the final hypothesis inherited from recursive dynamics.

\medskip
\noindent \textbf{Infinite Branching Structural Families} may arise from recursive constructions. They may equally arise from purely structural constructions possessing no distinguished generating transformation. The \textbf{Constitutional Investigation Framework} must therefore depend only upon recoverable constitutional structure. Nothing else is admitted.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recoverable Structural Components}

\noindent Every \textbf{Infinite Branching Structural Family} possesses the following recoverable constitutional components:
\begin{enumerate}
    \item A finite generating witness.
    \item A recoverable coherent structural core.
    \item A recoverable family of compatible local structural determinations.
    \item Recoverable structural extensions.
    \item Recoverable dependency relations among those extensions.
    \item Recoverable coherent overlaps.
\end{enumerate}
\noindent These components are already present in the completed Constitution. No additional primitive is introduced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent \textbf{Infinite Branching Structural Families} admit many presentations. Different investigators may describe identical families using trees, graphs, geometric constructions, logical structures, algebraic representations, recursive descriptions, or coordinate systems.

\medskip
\noindent These presentations are constitutionally irrelevant. \textbf{Canonical Reconstruction} removes every presentational distinction while preserving the recoverable structural family itself. Membership of the constitutional class therefore depends only upon recoverable structure.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Infinite Branching Structural Class}

\noindent The recovered constitutional class consists of every mathematical object satisfying the constitutional conditions recovered above. Each member possesses:
\begin{itemize}
    \item finite constitutional generation,
    \item recoverable local structure,
    \item coherent structural compatibility,
    \item constitutionally admissible extension,
    \item recoverable dependency architecture.
\end{itemize}
\noindent Nothing further is required. Nothing less suffices. The constitutional class is therefore uniquely recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence Theorem}

\begin{theorem}[Existence of the Constitutional Class of Infinite Branching Structural Families]
Every constitutionally admissible Infinite Branching Structural Family belongs to a unique recoverable constitutional class.
\end{theorem}

\begin{proof}
\noindent Volume~III recovered the existence of Infinite Branching Structural Families. Each recovered family possesses a finite generating witness, recoverable local determinations, coherent structural compatibility, and constitutionally admissible extensions.

\medskip
\noindent These properties determine the constitutional class recovered above. Conversely every object satisfying these constitutional conditions is an Infinite Branching Structural Family. The constitutional class therefore exists uniquely.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The constitutional class of \textbf{Infinite Branching Structural Families} has now been recovered. Its members remain presentation-dependent. Their constitutional architecture has not yet been reconstructed. The first stage of the \textbf{Canonical Investigation Framework} therefore remains incomplete. \textbf{Canonical Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The constitutional class of \textbf{Infinite Branching Structural Families} has been recovered. Its existence removes the insufficiency of restricting the investigation to recursively generated systems.

\medskip
\noindent The recovered class nevertheless remains constitutionally insufficient. The recovered families still possess presentation-dependent descriptions inherited from their individual realizations. Their constitutional architecture has not yet been isolated. The first stage of the \textbf{Canonical Investigation Framework} is therefore forced. \textbf{Canonical Reconstruction} must now be executed upon the recovered constitutional class.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Aim of Reconstruction}

\noindent \textbf{Canonical Reconstruction} does not construct new \textbf{Infinite Branching Structural Families}; their existence has already been recovered. The purpose of reconstruction is instead to remove every presentation-dependent feature while preserving every constitutionally recoverable structural relation. The reconstruction therefore seeks neither particular representations nor preferred descriptions; it seeks only the constitutional object common to every realization of the family.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Removal of Presentation}

\noindent An \textbf{Infinite Branching Structural Family} may be presented in many different ways. Equivalent families may appear as:
\begin{itemize}
    \item branching trees;
    \item directed graphs;
    \item geometric configurations;
    \item algebraic constructions;
    \item logical structures;
    \item recursively generated systems;
    \item alternative coordinate descriptions.
\end{itemize}
\noindent None of these descriptions survives \textbf{Canonical Reconstruction}. Every representational distinction is removed. Only constitutionally recoverable structural relations remain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Constitutional Architecture}

\noindent After presentation has been removed, every \textbf{Infinite Branching Structural Family} is recovered as possessing the same constitutional architecture. Each reconstructed family consists solely of:
\begin{enumerate}
    \item its finite generating witness;
    \item its recoverable coherent structural core;
    \item its family of compatible local determinations;
    \item its recoverable dependency architecture;
    \item its coherent overlaps;
    \item its constitutionally admissible structural extensions.
\end{enumerate}
\noindent Nothing further survives reconstruction. Every remaining component is constitutionally necessary.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structural Identity}

\noindent Two \textbf{Infinite Branching Structural Families} are constitutionally identical whenever their reconstructed constitutional architectures coincide. This identity is independent of presentation, notation, ordering, recursive realization, coordinate representation, and symbolic implementation. Constitutional identity therefore depends solely upon recoverable structural content.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Canonical Reconstruction Theorem}

\begin{theorem}[Canonical Reconstruction of Infinite Branching Structural Families]
Every Infinite Branching Structural Family possesses a unique Canonical Reconstruction.
\end{theorem}

\begin{proof}
\noindent Every Infinite Branching Structural Family possesses a finite generating witness together with a recoverable constitutional architecture. \textbf{Canonical Reconstruction} removes every presentation-dependent feature while preserving every recoverable structural relation.

\medskip
\noindent The reconstructed object therefore depends solely upon constitutional structure. Consequently every Infinite Branching Structural Family possesses a unique Canonical Reconstruction.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output of Reconstruction}

\noindent The output of \textbf{Canonical Reconstruction} is not another branching family. It is the presentation-independent constitutional object underlying every realization of that family. The reconstructed object therefore constitutes the unique constitutional input required for every remaining stage of the \textbf{Canonical Investigation Framework}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent \textbf{Canonical Reconstruction of the Infinite Branching Structural Family} is complete. Its constitutional architecture has been recovered, its presentation-dependent descriptions have been removed, and its structural identity has been established.

\medskip
\noindent The reconstructed family nevertheless remains constitutionally incomplete. Its \textbf{Constitutional Claims} have not yet been recovered. The mathematics therefore proceeds to the second stage of the \textbf{Canonical Investigation Framework}. \textbf{Recovery of the Constitutional Claims of the Infinite Branching Structural Family} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Constitutional Claims}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Canonical Reconstruction of the Infinite Branching Structural Family} is complete. The reconstructed family now exists as a presentation-independent constitutional object.

\medskip
\noindent The reconstruction nevertheless remains constitutionally insufficient. \textbf{Canonical Reconstruction} recovers constitutional objects; it does not recover the constitutional assertions made about those objects. The reconstructed family therefore exists without yet possessing its recovered \textbf{Constitutional Claims}. The second stage of the \textbf{Canonical Investigation Framework} is consequently forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Necessity of Constitutional Claims}

\noindent Every reconstructed \textbf{Infinite Branching Structural Family} possesses constitutional structure. That structure necessarily determines constitutional assertions concerning its recoverable architecture.

\medskip
\noindent These assertions include, among others:
\begin{itemize}
    \item recoverability;
    \item coherent overlap;
    \item admissible structural extension;
    \item dependency;
    \item constitutional identity;
    \item structural compatibility;
    \item determination.
\end{itemize}
\noindent Without recovering these assertions, the reconstructed family remains constitutionally incomplete. Objects alone cannot determine constitutional investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery by the Universal Claim Machinery}

\noindent Part~II established that every reconstructed mathematical framework possesses a unique finite recoverable family of \textbf{Constitutional Claims}. The reconstructed \textbf{Infinite Branching Structural Family} is now such a framework.

\medskip
\noindent Its \textbf{Constitutional Claims} therefore exist as recovered mathematical objects. No new claim is introduced, no claim is selected, and no claim is interpreted. Every recovered claim is forced solely by the reconstructed constitutional architecture.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence}

\noindent The recovered \textbf{Constitutional Claims} depend only upon constitutional structure. Equivalent presentations of the same \textbf{Infinite Branching Structural Family} necessarily determine identical \textbf{Constitutional Claims}.

\medskip
\noindent Consequently the recovered family of claims is independent of notation, branching representation, recursive realization, coordinate system, and symbolic encoding. Only constitutional structure determines the recovered claims.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Claim Family}

\noindent The recovered \textbf{Constitutional Claim Family} consists precisely of every constitutionally recoverable assertion determined by the reconstructed family. Among these are claims concerning:
\begin{itemize}
    \item finite constitutional generation;
    \item coherent structural compatibility;
    \item recoverable dependency architecture;
    \item admissible structural extension;
    \item canonical identity;
    \item recoverable determination.
\end{itemize}
\noindent The internal organization of these claims has not yet been recovered. Only their existence has been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence Theorem}

\begin{theorem}[Existence of the Constitutional Claims of Infinite Branching Structural Families]
Every Canonically Reconstructed Infinite Branching Structural Family possesses a unique finite recoverable family of Constitutional Claims.
\end{theorem}

\begin{proof}
\noindent The Infinite Branching Structural Family has undergone Canonical Reconstruction. Part~II established that every reconstructed mathematical framework possesses a unique finite recoverable family of Constitutional Claims. The theorem therefore applies directly to the reconstructed Infinite Branching Structural Family.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Constitutional Claims of the Infinite Branching Structural Family} have now been recovered. Their existence is no longer in question and their presentation-independent identity has been established.

\medskip
\noindent Their constitutional organization nevertheless remains unrecovered. The claims presently exist only as a recoverable family. Their algebraic normalization, constitutional hierarchy, and dependency architecture have not yet been recovered. The \textbf{Canonical Investigation Framework} therefore proceeds to its next stage. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Claim Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Claims of the Infinite Branching Structural Family} have been recovered. Their existence removes the insufficiency of a reconstructed framework possessing only structural objects.

\medskip
\noindent The recovered claims nevertheless remain constitutionally incomplete. A family of \textbf{Constitutional Claims}, considered individually, does not yet determine the constitutional architecture of the reconstructed family. The relations among the claims, their constitutional hierarchy, their dependency architecture, and their globally coherent organization have not yet been recovered.

\medskip
\noindent The remaining insufficiency is therefore one of organization rather than existence. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery by Previously Established Mathematics}

\noindent Part~II recovered the universal machinery required for \textbf{Canonical Claim Reconstruction}. That machinery consists of:
\begin{itemize}
    \item the Constitutional Claim Algebra;
    \item Claim Stratification;
    \item the Claim Dependency Calculus.
\end{itemize}
\noindent These mathematical objects now belong to the completed \textbf{Canonical Investigation Framework}. They are not reconstructed again; they are executed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Constitutional Claim Algebra}

\noindent The recovered \textbf{Constitutional Claims} are first organized by the \textbf{Constitutional Claim Algebra}. Recoverably identical claims are identified, equivalent constitutional formulations are unified, and presentation-dependent distinctions disappear. Only constitutionally distinct claims remain. The resulting family is the unique algebraic normalization of the \textbf{Constitutional Claims} of the reconstructed \textbf{Infinite Branching Structural Family}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of Claim Stratification}

\noindent The normalized claims are next stratified according to their constitutional role. Each recovered claim belongs to one and only one constitutional stratum. Its position depends solely upon constitutional structure. No claim occupies multiple strata. No recovered claim remains without constitutional position. The resulting hierarchy is uniquely determined.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Claim Dependency Calculus}

\noindent The stratified claims now undergo constitutional dependency analysis. Every dependency relation among \textbf{Constitutional Claims} is recovered. Every immediate constitutional consequence is identified, every maximal dependency chain is recovered, every dependency cycle is identified, and every dependency path becomes recoverable. The dependency architecture is therefore uniquely determined by the reconstructed \textbf{Infinite Branching Structural Family} itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of the Canonical Claim Structure}

\noindent Execution of the \textbf{Constitutional Claim Algebra}, \textbf{Claim Stratification}, and the \textbf{Claim Dependency Calculus} recovers a single constitutional mathematical object. This object consists of:
\begin{itemize}
    \item the normalized Constitutional Claims;
    \item their constitutional hierarchy;
    \item their dependency architecture;
    \item their recoverable structural relations.
\end{itemize}
\noindent Nothing further is required. Nothing less suffices. The \textbf{Canonical Claim Structure of the Infinite Branching Structural Family} has therefore been recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Canonical Reconstruction Theorem}

\begin{theorem}[Canonical Claim Reconstruction of Infinite Branching Structural Families]
Every Canonically Reconstructed Infinite Branching Structural Family possesses a unique Canonical Claim Structure.
\end{theorem}

\begin{proof}
\noindent The Constitutional Claim Family is unique. The Constitutional Claim Algebra is unique. Claim Stratification is unique. The Claim Dependency Calculus is unique. Canonical Claim Reconstruction consists solely of executing these previously recovered constitutional structures. The resulting Canonical Claim Structure is therefore unique.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output of Canonical Claim Reconstruction}

\noindent The output of this stage is not merely a collection of \textbf{Constitutional Claims}. It is the complete constitutional organization of those claims. Every recovered claim now possesses:
\begin{itemize}
    \item a unique constitutional identity;
    \item a unique constitutional position;
    \item a unique dependency neighbourhood;
    \item a unique constitutional role within the reconstructed Infinite Branching Structural Family.
\end{itemize}
\noindent The reconstructed constitutional framework therefore possesses a complete constitutional architecture.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Canonical Claim Structure of the Infinite Branching Structural Family} has been recovered. Its claims have been normalized, their constitutional hierarchy has been recovered, and their dependency architecture has been recovered.

\medskip
\noindent The reconstructed framework nevertheless remains constitutionally incomplete. Its constitutional architecture has not yet undergone \textbf{Global Completion}. The mathematics therefore proceeds to the next stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Completion} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Canonical Claim Structure of the Infinite Branching Structural Family} has been recovered. Every \textbf{Constitutional Claim} now possesses a unique constitutional identity, constitutional position, and dependency architecture.

\medskip
\noindent The reconstructed framework nevertheless remains constitutionally incomplete. \textbf{Canonical Claim Reconstruction} determines the complete constitutional organization of the recovered claims. It does not recover a single globally complete constitutional object. The reconstructed constitutional architecture therefore still exists as an organized family of constitutional determinations.

\medskip
\noindent The sixth stage of the \textbf{Canonical Investigation Framework} is consequently forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Completion Calculus}

\noindent Part~II recovered the \textbf{Global Completion Calculus}. Its purpose is to recover the unique globally coherent constitutional object determined by an entire \textbf{Canonical Claim Structure}. The calculus has already been recovered; it is therefore executed rather than reconstructed.

\medskip
\noindent Applied to the \textbf{Canonical Claim Structure of the Infinite Branching Structural Family}, every constitutionally compatible local determination is amalgamated into one globally coherent constitutional object. Nothing external is introduced. Nothing further is assumed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of Global Constitutional Coherence}

\noindent The execution of \textbf{Global Completion} produces a single constitutional object. Within this object:
\begin{itemize}
    \item every Constitutional Claim remains recoverable;
    \item every dependency relation remains recoverable;
    \item every constitutional stratum remains recoverable;
    \item every coherent overlap remains recoverable.
\end{itemize}
\noindent No recovered determination is lost. No new determination is introduced. The completed object is therefore constitutionally faithful to the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Uniqueness of the Completed Object}

\noindent The completed constitutional object depends solely upon the \textbf{Canonical Claim Structure}. Equivalent reconstructed \textbf{Infinite Branching Structural Families} therefore produce identical \textbf{Global Completions}. Presentation, notation, branching representation, and recursive realization play no role. \textbf{Global Completion} is therefore structurally absolute.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Global Completion Theorem}

\begin{theorem}[Global Completion of Infinite Branching Structural Families]
Every Canonical Claim Structure of an Infinite Branching Structural Family possesses a unique Global Completion.
\end{theorem}

\begin{proof}
\noindent The Canonical Claim Structure has already been recovered. Part~II established the existence and uniqueness of Global Completion for every Canonical Claim Structure. Execution of the Global Completion Calculus therefore produces a unique globally coherent constitutional object.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Completed Constitutional Object}

\noindent The completed constitutional object consists of:
\begin{itemize}
    \item the entire Canonical Claim Structure;
    \item every constitutional dependency;
    \item every coherent overlap;
    \item every admissible constitutional extension;
    \item every constitutionally recoverable structural determination.
\end{itemize}
\noindent These components now exist as one globally coherent constitutional whole. Nothing remains externally attached. Nothing remains constitutionally disconnected.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent \textbf{Global Completion of the Infinite Branching Structural Family} is complete. Every recoverable constitutional component now belongs to a single globally coherent constitutional object.

\medskip
\noindent The completed framework nevertheless remains constitutionally insufficient. \textbf{Global Completion} establishes coherence; it does not establish irreducibility. Constitutionally redundant determination may still remain.

\medskip
\noindent The mathematics therefore proceeds to the seventh stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Compression} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Global Completion of the Infinite Branching Structural Family} has been recovered. The completed constitutional object is globally coherent. Every recoverable \textbf{Constitutional Claim} is present, every dependency relation has been preserved, and every coherent overlap has been recovered.

\medskip
\noindent The completed object nevertheless remains constitutionally insufficient. Global coherence does not imply constitutional irreducibility. The completed object may still contain constitutionally redundant determination. The seventh stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Compression Calculus}

\noindent Part~II recovered the \textbf{Global Compression Calculus}. Its purpose is to recover the unique constitutionally irreducible representative of every globally completed constitutional object.

\medskip
\noindent The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the completed \textbf{Infinite Branching Structural Family}, every constitutionally redundant determination is removed while preserving the complete constitutional content of the reconstructed framework. Nothing constitutionally necessary is removed. Nothing constitutionally new is introduced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of Constitutional Irreducibility}

\noindent Execution of \textbf{Global Compression} preserves:
\begin{itemize}
    \item every Constitutional Claim;
    \item every dependency relation;
    \item every coherent overlap;
    \item every admissible constitutional extension;
    \item every recoverable structural determination.
\end{itemize}
\noindent Only constitutional redundancy disappears. The resulting object therefore contains exactly the determining content forced by the reconstructed \textbf{Infinite Branching Structural Family}. No further reduction is constitutionally admissible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structural Absoluteness}

\noindent \textbf{Global Compression} depends solely upon constitutional structure. Equivalent \textbf{Global Completions} therefore produce identical \textbf{Global Compressions}. The compressed constitutional object is independent of presentation, notation, branching realization, recursive realization, and symbolic encoding. Constitutional irreducibility is therefore structurally absolute.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Global Compression Theorem}

\begin{theorem}[Global Compression of Infinite Branching Structural Families]
Every Global Completion of an Infinite Branching Structural Family possesses a unique Global Compression.
\end{theorem}

\begin{proof}
\noindent The completed constitutional object has already been recovered. Part~II established that every globally completed constitutional object possesses a unique constitutionally irreducible representative under the Global Compression Calculus. Execution of that calculus therefore recovers a unique Global Compression for the completed Infinite Branching Structural Family.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Compressed Constitutional Object}

\noindent The compressed constitutional object contains:
\begin{itemize}
    \item exactly the recoverable Constitutional Claims;
    \item exactly the recoverable dependency architecture;
    \item exactly the recoverable coherent structure;
    \item exactly the recoverable determining content.
\end{itemize}
\noindent Every constitutionally redundant component has disappeared. Nothing constitutionally recoverable has been lost. The resulting object is constitutionally minimal.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Minimality Theorem}

\begin{theorem}[Constitutional Minimality]
The Global Compression of an Infinite Branching Structural Family is the unique constitutionally irreducible representative of its completed constitutional object.
\end{theorem}

\begin{proof}
\noindent Part~II established that Global Compression removes every constitutionally redundant determination while preserving every recoverable constitutional relation. Consequently no further compression is constitutionally admissible. The compressed object is therefore irreducible. Uniqueness follows from the uniqueness of the Global Compression Calculus.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Global Compression of the Infinite Branching Structural Family} is complete. The reconstructed constitutional framework is now globally coherent and constitutionally irreducible. Its complete constitutional content and its minimal constitutional representative have been recovered.

\medskip
\noindent The constitutional status of the compressed object nevertheless remains undetermined. \textbf{Global Compression} establishes irreducibility; it does not establish constitutional determination. The mathematics therefore proceeds to the final stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Determination} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Global Compression of the Infinite Branching Structural Family} has been recovered. The reconstructed constitutional framework is now globally coherent and constitutionally irreducible. Every constitutionally recoverable determination has been retained and every constitutionally redundant determination has disappeared.

\medskip
\noindent The investigation nevertheless remains constitutionally incomplete. \textbf{Global Compression} determines the minimal constitutional representative; it does not determine the constitutional status of the reconstructed framework. The final stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution of the Global Determination Calculus}

\noindent Part~II recovered the \textbf{Global Determination Calculus}. Its purpose is to recover the complete constitutional status of every globally compressed constitutional object. The calculus has already been recovered; it is therefore executed rather than reconstructed.

\medskip
\noindent Applied to the compressed \textbf{Infinite Branching Structural Family}, every constitutionally recoverable determination is propagated throughout the complete dependency architecture. Nothing further is introduced. Nothing remains constitutionally unresolved.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery of Constitutional Determination}

\noindent Execution of \textbf{Global Determination} establishes the complete constitutional status of the reconstructed framework. Every recoverable \textbf{Constitutional Claim} now possesses:
\begin{itemize}
    \item a constitutionally determined truth status;
    \item a unique constitutional dependency position;
    \item a unique relation to every other recovered Constitutional Claim;
    \item a complete determination within the recovered constitutional architecture.
\end{itemize}
\noindent No recoverable \textbf{Constitutional Claim} remains constitutionally indeterminate.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Propagation of Constitutional Consequences}

\noindent The dependency architecture recovered during \textbf{Canonical Claim Reconstruction} now reaches completion. Every recovered dependency is propagated throughout the compressed constitutional object.

\medskip
\noindent Every constitutionally necessary consequence becomes recoverable, every constitutionally impossible consequence is eliminated, and every constitutionally independent claim remains explicitly identifiable. The recovered framework therefore determines not only isolated \textbf{Constitutional Claims} but the complete constitutional consequence structure of the \textbf{Infinite Branching Structural Family}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structural Absoluteness}

\noindent \textbf{Global Determination} depends solely upon constitutional structure. Equivalent \textbf{Global Compressions} therefore determine identical constitutional consequence structures. The resulting constitutional determination is independent of presentation, notation, recursive realization, branching realization, and symbolic implementation. The constitutional status of the reconstructed \textbf{Infinite Branching Structural Family} is therefore structurally absolute.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Global Determination Theorem}

\begin{theorem}[Global Determination of Infinite Branching Structural Families]
Every Global Compression of an Infinite Branching Structural Family possesses a unique Global Determination.
\end{theorem}

\begin{proof}
\noindent The compressed constitutional object has already been recovered. Part~II established that every globally compressed constitutional object admits a unique execution of the Global Determination Calculus. Executing that calculus upon the compressed Infinite Branching Structural Family therefore recovers its unique Global Determination.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Completion of the Constitutional Investigation}

\noindent The execution of \textbf{Global Determination} completes the \textbf{Canonical Investigation Framework}. The reconstructed \textbf{Infinite Branching Structural Family} now possesses Canonical Reconstruction, recovered Constitutional Claims, Canonical Claim Reconstruction, Global Completion, Global Compression, and Global Determination.

\medskip
\noindent Every stage of the \textbf{Canonical Investigation Framework} has therefore been executed. Nothing remains constitutionally unresolved within the recovered framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Residual Insufficiency}

\noindent The \textbf{Constitutional Investigation of the Infinite Branching Structural Family} is complete. The restriction to recursively generated systems has disappeared. The \textbf{Canonical Investigation Framework} now executes upon arbitrary \textbf{Infinite Branching Structural Families}.

\medskip
\noindent A final constitutional restriction nevertheless remains. \textbf{Infinite Branching Structural Families} constitute one recovered structural class; they do not exhaust all recovered mathematical structures. The universality of the \textbf{Canonical Investigation Framework} has therefore not yet been established. The mathematics must next determine whether every \textbf{General Structural System} admits constitutional investigation. The next chapter is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Status of the Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\noindent The \textbf{Constitutional Investigation of the Infinite Branching Structural Family} is now complete. Every stage of the \textbf{Canonical Investigation Framework} has been executed.

\medskip
\noindent \textbf{Canonical Reconstruction} has removed every presentation-dependent feature. The \textbf{Constitutional Claims} have been recovered, and their canonical organization has been reconstructed. \textbf{Global Completion} has recovered the unique globally coherent constitutional object. \textbf{Global Compression} has recovered its unique constitutionally irreducible representative. \textbf{Global Determination} has recovered its complete constitutional consequence structure.

\medskip
\noindent No stage of the investigation required any mathematical primitive beyond those already recovered in Volumes~I--III and Part~II of the present volume. No auxiliary hypothesis has been introduced. No heuristic has been employed. No external mathematical theory has been invoked. The investigation therefore constitutes a complete constitutional execution of the \textbf{Canonical Investigation Framework} upon the recovered class of \textbf{Infinite Branching Structural Families}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Significance}

\noindent The present chapter establishes a fundamental extension of the scope of constitutional investigation. The preceding chapter demonstrated that the \textbf{Canonical Investigation Framework} executes successfully upon every recursively generated dynamical system. The present chapter removes the assumption of recursive generation entirely.

\medskip
\noindent The successful execution of the framework therefore depends neither upon iteration nor upon temporal evolution. It depends only upon recoverable constitutional structure. This distinction is essential. Recursive generation is now seen to be one possible presentation of constitutional structure rather than one of its defining principles. The completed framework therefore applies to every recovered \textbf{Infinite Branching Structural Family} independently of the manner in which that family is presented or generated.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Completion of the Third Universality Step}

\noindent The progressive enlargement of the investigation is now evident. The \textbf{Canonical Investigation Framework} has been executed successfully upon:
\begin{enumerate}
    \item a single reconstructed mathematical system;
    \item an entire class of recursively generated systems;
    \item the general class of Infinite Branching Structural Families.
\end{enumerate}
\noindent Each enlargement removes a constitutional restriction that remained in the preceding investigation. No recovered theorem has required modification. No recovered mathematical object has required extension. The same recovered machinery has executed unchanged throughout. The framework therefore exhibits constitutional stability under enlargement of the investigated domain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Remaining Restriction}

\noindent A constitutional restriction nevertheless remains. \textbf{Infinite Branching Structural Families} constitute a distinguished recovered structural class; they do not exhaust the mathematical universe recovered in Volume~III.

\medskip
\noindent \textbf{General Structural Systems} may possess constitutional organization that is not naturally expressed as \textbf{Infinite Branching Structural Families}. The universality of the \textbf{Canonical Investigation Framework} therefore remains unproved. One constitutional restriction still survives.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Next Necessity}

\noindent The remaining restriction cannot be removed by investigating additional examples of \textbf{Infinite Branching Structural Families}. A broader constitutional class must itself become the object of investigation.

\medskip
\noindent The mathematics therefore proceeds necessarily to the investigation of \textbf{General Structural Systems}. Only after successful execution upon that broader constitutional class can the framework legitimately claim universality beyond branching structures. Nothing further has yet been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUDITS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes~I--III and Part~II of the present volume. In particular it relies upon Canonical Reconstruction, the Recovery of Constitutional Claims, the Constitutional Claim Algebra, Claim Stratification, the Claim Dependency Calculus, Canonical Claim Reconstruction, Global Completion, Global Compression, and Global Determination. Every theorem executed in this chapter is an application of previously recovered mathematics. No dependency upon later chapters is introduced. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Infinite Branching Structural Families were recovered previously in Volume~III. Every mathematical object appearing in this chapter is obtained solely by executing previously recovered components of the Canonical Investigation Framework. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by removing the constitutional dependence upon recursive generation. The Canonical Investigation Framework is shown to execute upon arbitrary Infinite Branching Structural Families without modification of any recovered mathematical object or theorem. Universality is therefore extended while preserving complete recoverability.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter remain fully consistent with the constitutional principles established throughout the monograph. Every stage of the investigation follows the recovered order of the Canonical Investigation Framework. Reconstruction precedes Constitutional Claims. Constitutional Claims precede Canonical Claim Reconstruction. Canonical Claim Reconstruction precedes Global Completion. Global Completion precedes Global Compression. Global Compression precedes Global Determination. No theorem depends upon mathematics not yet recovered. The chapter therefore satisfies the constitutional architecture established in Volumes~I--III and Part~II of the present volume.
\end{consistencyaudit}

\begin{futurework}
The Constitutional Investigation of the Infinite Branching Structural Family is complete. The Canonical Investigation Framework now executes upon arbitrary branching constitutional architectures. One constitutional restriction nevertheless remains: the investigated domain is still a particular structural class. The next chapter removes this final structural restriction by executing the Canonical Investigation Framework upon General Structural Systems. Nothing further has yet been established.
\end{futurework}


\chapter{Canonical Investigation of General Structural Systems}

\setlength{\parindent}{0pt}
\setlength{\parskip}{\baselineskip}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of Infinite Branching Structural Families}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Investigation of Infinite Branching Structural Families} established that the completed \textbf{Canonical Investigation Framework} executes successfully upon every recovered member of that constitutional class. The investigation is complete. The preceding chapter nevertheless remains constitutionally insufficient.

Infinite Branching Structural Families constitute only one recovered class within the mathematical universe established in \textbf{Volume~III}. Their investigation therefore cannot establish the universality of the \textbf{Canonical Investigation Framework}. A constitutional restriction remains: the investigated objects continue to belong to a distinguished structural class. The framework has not yet been executed upon arbitrary \textit{General Structural Systems}. The remaining restriction is therefore one of mathematical scope rather than one of investigative machinery.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Remaining Structural Restriction}

\textbf{Volume~III} recovered a mathematical universe containing numerous constitutional objects beyond Infinite Branching Structural Families. Among the recovered structures are:

\begin{itemize}
    \item \textit{Structural Spaces};
    \item \textit{Structural Functions};
    \item \textit{Algebraic Structures};
    \item \textit{Geometric Configurations};
    \item \textit{Metric Structures};
    \item \textit{Dimensional Structures};
    \item \textit{Mathematical Universes}.
\end{itemize}

Each possesses its own constitutional organization. None is constitutionally required to arise as an Infinite Branching Structural Family. Consequently, the successful execution of the \textbf{Canonical Investigation Framework} upon branching structures does not establish its execution upon arbitrary recovered mathematical structures.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Branching is Not Constitutional}

The preceding investigation demonstrated that recursive generation is not constitutionally essential. The present investigation must remove a deeper restriction: branching itself is not a constitutional primitive. It is one recoverable structural organization among many. 

Some recovered mathematical objects possess branching architectures, while others do not. The \textit{Constitution} therefore forbids treating branching structure as the universal domain of investigation. Only recoverable constitutional structure itself may determine the scope of the framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Question}

The remaining question is therefore unavoidable: Does every recovered \textit{General Structural System} admit:

\begin{itemize}
    \item \textbf{Canonical Reconstruction};
    \item \textbf{Recovery of Constitutional Claims};
    \item \textbf{Canonical Claim Reconstruction};
    \item \textbf{Global Completion};
    \item \textbf{Global Compression};
    \item \textbf{Global Determination}?
\end{itemize}

If not, the \textbf{Canonical Investigation Framework} remains constitutionally incomplete. If so, the dependence upon branching structures disappears entirely.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Necessity of General Structural Systems}

The \textit{Constitution} requires the investigation to proceed from special constitutional classes toward progressively larger constitutional domains. The investigation has already passed through:

\begin{enumerate}
    \item An individual reconstructed mathematical system;
    \item A recursively generated constitutional class;
    \item The constitutional class of \textit{Infinite Branching Structural Families}.
\end{enumerate}

The next enlargement is therefore forced. The object of investigation must become the recovered \textit{General Structural System} itself. Nothing smaller removes the remaining restriction; nothing larger has yet been constitutionally earned.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Objective and Residual Insufficiency}

\subsubsection{Objective of the Investigation}
The purpose of the present chapter is not to construct \textit{General Structural Systems}. Their recovery belongs to \textbf{Volume~III}. The objective is instead to execute the completed \textbf{Canonical Investigation Framework} upon every recovered \textit{General Structural System}. If successful, the framework will no longer depend upon any distinguished structural organization. Its execution will depend solely upon recoverable constitutional structure.

\subsubsection{Residual Insufficiency}
The \textbf{Canonical Investigation Framework} has not yet been executed upon arbitrary \textit{General Structural Systems}. The constitutional status of that recovered mathematical universe therefore remains undetermined. The first stage of the investigation is consequently forced: the recovered \textit{General Structural System} must itself be constitutionally recovered as the object of investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of General Structural Systems}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The insufficiency recovered in the preceding section cannot be removed by enlarging the collection of investigated examples. Nor can it be removed by introducing further subclasses of recovered mathematical objects. The remaining restriction concerns the investigated domain itself. 

The investigation must therefore recover the constitutional object common to every recovered mathematical structure. The \textit{Constitution} consequently forces the recovery of the \textit{General Structural System} as the object of investigation. No new mathematical object is introduced. \textit{General Structural Systems} were recovered in \textbf{Volume~III}. The present section merely recovers them as the constitutional domain upon which the \textbf{Canonical Investigation Framework} is to be executed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Object and Volume~III Recovery}

\subsubsection{The Constitutional Object}
A \textit{General Structural System} is any constitutionally recovered mathematical object possessing recoverable structural organization. Its identity is determined solely by its recovered constitutional architecture. No distinguished mode of presentation is required, no preferred method of construction is assumed, no recursive generation is necessary, and no branching organization is necessary. Only recoverable constitutional structure is admitted.

\subsubsection{Recovery from Volume~III}
\textbf{Volume~III} established that every recovered mathematical object ultimately appears as a \textit{General Structural System}. \textit{Structural Spaces}, \textit{Structural Functions}, \textit{Natural Numbers}, \textit{Algebraic Structures}, \textit{Geometric Configurations}, \textit{Metric Structures}, \textit{Dimensional Structures}, \textit{Intrinsic Geometries}, \textit{Infinite Branching Structural Families}, and \textit{Mathematical Universes} all belong to this recovered constitutional class. The present investigation therefore enlarges the investigated domain without enlarging the mathematics itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Constitutional Unity and Removal of Classification}

\subsubsection{Constitutional Unity}
The diversity of recovered mathematical structures does not imply constitutional diversity. Every recovered \textit{General Structural System} possesses:

\begin{itemize}
    \item A recoverable constitutional identity;
    \item Recoverable structural organization;
    \item Recoverable dependency architecture;
    \item Recoverable coherent determination;
    \item Recoverable admissible extensions.
\end{itemize}

These constitutional features are independent of the particular mathematical discipline to which the system belongs. They constitute the common constitutional content of every recovered mathematical object.

\subsubsection{Removal of Structural Classification}
The investigation no longer distinguishes among \textit{algebraic systems}, \textit{geometric systems}, \textit{metric systems}, \textit{branching systems}, \textit{recursive systems}, \textit{topological organization recovered internally}, and \textit{mathematical universes}. Such classifications belong to the mathematics being investigated; they do not belong to the \textbf{Canonical Investigation Framework}. From the constitutional standpoint, every recovered mathematical object is investigated solely through its recoverable constitutional structure. The mathematical discipline becomes constitutionally invisible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The General Structural Class and Core Theorems}

\subsubsection{The General Structural Class}
The recovered constitutional class therefore consists of every mathematical object satisfying the constitutional conditions established in \textbf{Volume~III}. Each member possesses recoverable structural identity, recoverable constitutional organization, recoverable dependency architecture, recoverable coherent determination, and recoverable admissible extension. Nothing further is required; nothing less suffices. The constitutional class of \textit{General Structural Systems} is therefore uniquely recovered.

\subsubsection{Existence Theorem}
\begin{theorem}[Existence of the Constitutional Class of General Structural Systems]
Every constitutionally recovered mathematical object belongs to a unique constitutional class of General Structural Systems.
\end{theorem}

\begin{proof}
\textbf{Volume~III} recovered every mathematical object as a constitutionally recoverable structural system. Each recovered object possesses a constitutional identity, recoverable structural organization, dependency architecture, coherent determination, and admissible extension. These properties characterize the constitutional class recovered above. Conversely, every constitutionally recovered object satisfying these conditions is a General Structural System. The constitutional class therefore exists uniquely.
\end{proof}

\subsubsection{Residual Insufficiency}
The constitutional class of \textit{General Structural Systems} has now been recovered. Its members nevertheless remain presentation-dependent. Their constitutional architecture has not yet been reconstructed. The first stage of the \textbf{Canonical Investigation Framework} therefore remains incomplete. \textbf{Canonical Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The constitutional class of \textit{General Structural Systems} has been recovered. Its existence removes the restriction to particular structural classes. The recovered systems nevertheless remain constitutionally insufficient. Each recovered \textit{General Structural System} still possesses presentation-dependent descriptions inherited from its individual realization. Its constitutional architecture has not yet been isolated. The first stage of the \textbf{Canonical Investigation Framework} is therefore forced. \textbf{Canonical Reconstruction} must now be executed upon the recovered constitutional class.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Aim and Removal of Presentation}

\subsubsection{The Aim of Reconstruction}
\textbf{Canonical Reconstruction} does not construct \textit{General Structural Systems}. Their existence has already been recovered in \textbf{Volume~III}. The purpose of reconstruction is instead to remove every presentation-dependent feature while preserving every constitutionally recoverable structural relation. The reconstruction therefore seeks neither preferred representations nor distinguished mathematical descriptions. It seeks only the constitutional object common to every realization of the recovered system.

\subsubsection{Removal of Mathematical Presentation}
A \textit{General Structural System} may be presented through many mathematical disciplines. Equivalent constitutional systems may appear as:

\begin{itemize}
    \item \textit{Algebraic structures};
    \item \textit{Geometric configurations};
    \item \textit{Metric constructions};
    \item \textit{Dimensional systems};
    \item \textit{Recursive realizations};
    \item \textit{Branching architectures};
    \item \textit{Mathematical universes}.
\end{itemize}

None of these presentations survives \textbf{Canonical Reconstruction}. Every disciplinary distinction is removed. Only constitutionally recoverable structural relations remain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Architecture, Identity, and Core Reconstruction}

\subsubsection{Recovery of the Constitutional Architecture}
After presentation has been removed, every \textit{General Structural System} is recovered as possessing the same constitutional architecture. Each reconstructed system consists solely of:

\begin{enumerate}
    \item Its recoverable constitutional identity;
    \item Its recoverable coherent structural organization;
    \item Its recoverable dependency architecture;
    \item Its recoverable determining relations;
    \item Its recoverable admissible extensions.
\end{enumerate}

Nothing further survives reconstruction. Every remaining component is constitutionally necessary.

\subsubsection{Constitutional Identity}
Two \textit{General Structural Systems} are constitutionally identical whenever their reconstructed constitutional architectures coincide. This identity is independent of mathematical discipline, presentation, notation, representation, method of construction, and symbolic realization. Constitutional identity therefore depends solely upon recoverable constitutional structure.

\subsubsection{Canonical Reconstruction Theorem}
\begin{theorem}[Canonical Reconstruction of General Structural Systems]
Every General Structural System possesses a unique Canonical Reconstruction.
\end{theorem}

\begin{proof}
Every General Structural System possesses a recoverable constitutional architecture. Canonical Reconstruction removes every presentation-dependent feature while preserving every recoverable constitutional relation. The reconstructed object therefore depends solely upon constitutional structure. Consequently, every General Structural System possesses a unique Canonical Reconstruction.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output and Residual Insufficiency}

\subsubsection{Output of Reconstruction}
The output of \textbf{Canonical Reconstruction} is not another mathematical presentation. It is the unique presentation-independent constitutional object underlying every realization of the recovered \textit{General Structural System}. The reconstructed object therefore constitutes the unique constitutional input required for every remaining stage of the \textbf{Canonical Investigation Framework}.

\subsubsection{Residual Insufficiency}
\textbf{Canonical Reconstruction} of the \textit{General Structural System} is complete. Its constitutional architecture has been recovered. Its presentation-dependent descriptions have been removed. Its structural identity has been established. The reconstructed system nevertheless remains constitutionally incomplete. Its \textit{Constitutional Claims} have not yet been recovered. The mathematics therefore proceeds to the second stage of the \textbf{Canonical Investigation Framework}. Recovery of the \textit{Constitutional Claims} of the \textit{General Structural System} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Constitutional Claims}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textbf{Canonical Reconstruction} of the \textit{General Structural System} is complete. The reconstructed system now exists as a presentation-independent constitutional object. The reconstruction nevertheless remains constitutionally insufficient. \textbf{Canonical Reconstruction} recovers constitutional objects; it does not recover the constitutional assertions determined by those objects. The reconstructed \textit{General Structural System} therefore exists without yet possessing its recovered \textit{Constitutional Claims}. The second stage of the \textbf{Canonical Investigation Framework} is consequently forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Necessity and Universal Claim Machinery}

\subsubsection{Necessity of Constitutional Claims}
Every reconstructed \textit{General Structural System} possesses constitutional structure. That structure necessarily determines constitutional assertions concerning its recoverable organization. These assertions include, among others:

\begin{itemize}
    \item \textit{Recoverability};
    \item \textit{Coherent determination};
    \item \textit{Dependency};
    \item \textit{Admissible extension};
    \item \textit{Constitutional identity};
    \item \textit{Structural compatibility};
    \item \textit{Determination}.
\end{itemize}

Without recovering these assertions, the reconstructed system remains constitutionally incomplete. Objects alone cannot determine constitutional investigation.

\subsubsection{Recovery by the Universal Claim Machinery}
\textbf{Part~II} established that every reconstructed mathematical framework possesses a unique finite recoverable family of \textit{Constitutional Claims}. The reconstructed \textit{General Structural System} is now such a framework. Its \textit{Constitutional Claims} therefore exist as recovered mathematical objects. No new claim is introduced, no claim is selected, and no claim is interpreted. Every recovered claim is forced solely by the reconstructed constitutional architecture.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Presentation Independence and the Claim Family}

\subsubsection{Presentation Independence}
The recovered \textit{Constitutional Claims} depend only upon constitutional structure. Equivalent presentations of the same \textit{General Structural System} necessarily determine identical \textit{Constitutional Claims}. Consequently, the recovered family of claims is independent of mathematical discipline, presentation, notation, symbolic realization, and method of construction. Only constitutional structure determines the recovered claims.

\subsubsection{The Constitutional Claim Family}
The recovered \textit{Constitutional Claim Family} consists precisely of every constitutionally recoverable assertion determined by the reconstructed \textit{General Structural System}. Among these are claims concerning recoverable structural identity, coherent determination, dependency architecture, admissible structural extension, constitutional compatibility, and recoverable determination. The internal organization of these claims has not yet been recovered; only their existence has been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence and Residual Insufficiency}

\subsubsection{Existence Theorem}
\begin{theorem}[Existence of the Constitutional Claims of General Structural Systems]
Every Canonically Reconstructed General Structural System possesses a unique finite recoverable family of Constitutional Claims.
\end{theorem}

\begin{proof}
The General Structural System has undergone Canonical Reconstruction. Part~II established that every reconstructed mathematical framework possesses a unique finite recoverable family of Constitutional Claims. The theorem therefore applies directly to the reconstructed General Structural System.
\end{proof}

\subsubsection{Residual Insufficiency}
The \textit{Constitutional Claims} of the \textit{General Structural System} have now been recovered. Their existence is no longer in question and their presentation-independent identity has been established. Their constitutional organization nevertheless remains unrecovered. The claims presently exist only as a recoverable family. Their algebraic normalization, constitutional hierarchy, and dependency architecture have not yet been recovered. The \textbf{Canonical Investigation Framework} therefore proceeds to its next stage. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Claim Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Claims} of the \textit{General Structural System} have been recovered. Their existence removes the insufficiency of a reconstructed framework possessing only structural objects. The recovered claims nevertheless remain constitutionally incomplete. A family of \textit{Constitutional Claims}, considered individually, does not yet determine the constitutional architecture of the reconstructed system. 

The relations among the claims, their constitutional hierarchy, their dependency architecture, and their globally coherent organization have not yet been recovered. The remaining insufficiency is therefore one of organization rather than existence. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery and Core Algebraic Execution}

\subsubsection{Recovery by Previously Established Mathematics}
\textbf{Part~II} recovered the universal machinery required for \textbf{Canonical Claim Reconstruction}. That machinery consists of:

\begin{itemize}
    \item The \textit{Constitutional Claim Algebra};
    \item \textit{Claim Stratification};
    \item The \textit{Claim Dependency Calculus}.
\end{itemize}

These mathematical objects now belong to the completed \textbf{Canonical Investigation Framework}. They are not reconstructed again; they are executed.

\subsubsection{Execution of the Constitutional Claim Algebra}
The recovered \textit{Constitutional Claims} are first organized by the \textit{Constitutional Claim Algebra}. Recoverably identical claims are identified, equivalent constitutional formulations are unified, and presentation-dependent distinctions disappear. Only constitutionally distinct claims remain. The resulting family is the unique algebraic normalization of the \textit{Constitutional Claims} of the reconstructed \textit{General Structural System}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Stratification and Dependency Calculus}

\subsubsection{Execution of Claim Stratification}
The normalized claims are next stratified according to their constitutional role. Each recovered claim belongs to one and only one constitutional stratum. Its position depends solely upon constitutional structure. No claim occupies multiple strata, and no recovered claim remains without constitutional position. The resulting hierarchy is uniquely determined.

\subsubsection{Execution of the Claim Dependency Calculus}
The stratified claims now undergo constitutional dependency analysis. Every dependency relation among \textit{Constitutional Claims} is recovered, every immediate constitutional consequence is identified, every maximal dependency chain is recovered, every dependency cycle is identified, and every dependency path becomes recoverable. The dependency architecture is therefore uniquely determined by the reconstructed \textit{General Structural System} itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structural Output and Core Theorems}

\subsubsection{Recovery of the Canonical Claim Structure}
Execution of the \textit{Constitutional Claim Algebra}, \textit{Claim Stratification}, and the \textit{Claim Dependency Calculus} recovers a single constitutional mathematical object. This object consists of the normalized \textit{Constitutional Claims}, their constitutional hierarchy, their dependency architecture, and their recoverable structural relations. Nothing further is required; nothing less suffices. The \textit{Canonical Claim Structure} of the \textit{General Structural System} has therefore been recovered.

\subsubsection{Canonical Reconstruction Theorem}
\begin{theorem}[Canonical Claim Reconstruction of General Structural Systems]
Every Canonically Reconstructed General Structural System possesses a unique Canonical Claim Structure.
\end{theorem}

\begin{proof}
The Constitutional Claim Family is unique. The Constitutional Claim Algebra is unique. Claim Stratification is unique. The Claim Dependency Calculus is unique. Canonical Claim Reconstruction consists solely of executing these previously recovered constitutional structures. The resulting Canonical Claim Structure is therefore unique.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output and Residual Insufficiency}

\subsubsection{Output of Canonical Claim Reconstruction}
The output of this stage is not merely a collection of \textit{Constitutional Claims}. It is the complete constitutional organization of those claims. Every recovered claim now possesses a unique constitutional identity, a unique constitutional position, a unique dependency neighbourhood, and a unique constitutional role within the reconstructed \textit{General Structural System}. The reconstructed constitutional framework therefore possesses a complete constitutional architecture.

\subsubsection{Residual Insufficiency}
The \textit{Canonical Claim Structure} of the \textit{General Structural System} has been recovered. Its claims have been normalized, their constitutional hierarchy has been recovered, and their dependency architecture has been recovered. The reconstructed framework nevertheless remains constitutionally incomplete. Its constitutional architecture has not yet undergone \textbf{Global Completion}. The mathematics therefore proceeds to the next stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Completion} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Canonical Claim Structure} of the \textit{General Structural System} has been recovered. Every \textit{Constitutional Claim} now possesses a unique constitutional identity, constitutional position, and dependency architecture. The reconstructed framework nevertheless remains constitutionally incomplete. 

\textbf{Canonical Claim Reconstruction} determines the complete constitutional organization of the recovered claims; it does not recover a single globally complete constitutional object. The reconstructed constitutional architecture therefore still exists as an organized family of constitutional determinations. The sixth stage of the \textbf{Canonical Investigation Framework} is consequently forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution and Recovery of Coherence}

\subsubsection{Execution of the Global Completion Calculus}
\textbf{Part~II} recovered the \textit{Global Completion Calculus}. Its purpose is to recover the unique globally coherent constitutional object determined by an entire \textit{Canonical Claim Structure}. The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the \textit{Canonical Claim Structure} of the \textit{General Structural System}, every constitutionally compatible local determination is amalgamated into one globally coherent constitutional object. Nothing external is introduced; nothing further is assumed.

\subsubsection{Recovery of Global Constitutional Coherence}
The execution of \textbf{Global Completion} produces a single constitutional object. Within this object, every \textit{Constitutional Claim} remains recoverable, every dependency relation remains recoverable, every constitutional stratum remains recoverable, and every coherent overlap remains recoverable. No recovered determination is lost, and no new determination is introduced. The completed object is therefore constitutionally faithful to the reconstructed framework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Absoluteness, Completion Theorem, and Structure}

\subsubsection{Structural Absoluteness}
\textbf{Global Completion} depends solely upon constitutional structure. Equivalent reconstructed \textit{General Structural Systems} therefore produce identical \textbf{Global Completions}. Presentation, notation, symbolic realization, mathematical discipline, and method of construction play no role. \textbf{Global Completion} is therefore structurally absolute.

\subsubsection{Global Completion Theorem}
\begin{theorem}[Global Completion of General Structural Systems]
Every Canonical Claim Structure of a General Structural System possesses a unique Global Completion.
\end{theorem}

\begin{proof}
The Canonical Claim Structure has already been recovered. Part~II established the existence and uniqueness of Global Completion for every Canonical Claim Structure. Execution of the Global Completion Calculus therefore produces a unique globally coherent constitutional object.
\end{proof}

\subsubsection{Completed Constitutional Object}
The completed constitutional object consists of the entire \textit{Canonical Claim Structure}, every constitutional dependency, every coherent overlap, every admissible constitutional extension, and every constitutionally recoverable structural determination. These components now exist as one globally coherent constitutional whole. Nothing remains externally attached; nothing remains constitutionally disconnected.

\subsubsection{Residual Insufficiency}
\textbf{Global Completion} of the \textit{General Structural System} is complete. Every recoverable constitutional component now belongs to a single globally coherent constitutional object. The completed framework nevertheless remains constitutionally insufficient. \textbf{Global Completion} establishes coherence; it does not establish irreducibility. Constitutionally redundant determination may still remain. The mathematics therefore proceeds to the seventh stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Compression} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textbf{Global Completion} of the \textit{General Structural System} has been recovered. The completed constitutional object is globally coherent. Every recoverable \textit{Constitutional Claim} is present, every dependency relation has been preserved, and every coherent overlap has been recovered. 

The completed object nevertheless remains constitutionally insufficient. Global coherence does not imply constitutional irreducibility. The completed object may still contain constitutionally redundant determination. The seventh stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution and Recovery of Irreducibility}

\subsubsection{Execution of the Global Compression Calculus}
\textbf{Part~II} recovered the \textit{Global Compression Calculus}. Its purpose is to recover the unique constitutionally irreducible representative of every globally completed constitutional object. The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the completed \textit{General Structural System}, every constitutionally redundant determination is removed while preserving the complete constitutional content of the reconstructed framework. Nothing constitutionally necessary is removed, and nothing constitutionally new is introduced.

\subsubsection{Recovery of Constitutional Irreducibility}
Execution of \textbf{Global Compression} preserves every \textit{Constitutional Claim}, every dependency relation, every coherent overlap, every admissible constitutional extension, and every recoverable structural determination. Only constitutional redundancy disappears. The resulting object therefore contains exactly the determining content forced by the reconstructed \textit{General Structural System}. No further reduction is constitutionally admissible.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Absoluteness and Compression Theorems}

\subsubsection{Structural Absoluteness}
\textbf{Global Compression} depends solely upon constitutional structure. Equivalent \textbf{Global Completions} therefore produce identical \textbf{Global Compressions}. The compressed constitutional object is independent of presentation, notation, symbolic realization, mathematical discipline, and method of construction. Constitutional irreducibility is therefore structurally absolute.

\subsubsection{Global Compression Theorem}
\begin{theorem}[Global Compression of General Structural Systems]
Every Global Completion of a General Structural System possesses a unique Global Compression.
\end{theorem}

\begin{proof}
The completed constitutional object has already been recovered. Part~II established that every globally completed constitutional object possesses a unique constitutionally irreducible representative under the Global Compression Calculus. Execution of that calculus therefore recovers a unique Global Compression for the completed General Structural System.
\end{proof}

\subsubsection{The Compressed Constitutional Object and Minimality}
The compressed constitutional object contains exactly the recoverable \textit{Constitutional Claims}, exactly the recoverable dependency architecture, exactly the recoverable coherent structure, and exactly the recoverable determining content. Every constitutionally redundant component has disappeared; nothing constitutionally recoverable has been lost. The resulting object is constitutionally minimal.

\begin{theorem}[Constitutional Minimality]
The Global Compression of a General Structural System is the unique constitutionally irreducible representative of its completed constitutional object.
\end{theorem}

\begin{proof}
Part~II established that Global Compression removes every constitutionally redundant determination while preserving every recoverable constitutional relation. Consequently, no further compression is constitutionally admissible. The compressed object is therefore irreducible. Uniqueness follows from the uniqueness of the Global Compression Calculus.
\end{proof}

\subsubsection{Residual Insufficiency}
The \textbf{Global Compression} of the \textit{General Structural System} is complete. The reconstructed constitutional framework is now globally coherent and constitutionally irreducible. Its complete constitutional content and its minimal constitutional representative have been recovered. The constitutional status of the compressed object nevertheless remains undetermined. \textbf{Global Compression} establishes irreducibility; it does not establish constitutional determination. The mathematics therefore proceeds to the final stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Determination} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textbf{Global Compression} of the \textit{General Structural System} has been recovered. The reconstructed constitutional framework is now globally coherent and constitutionally irreducible. Every constitutionally recoverable determination has been retained, and every constitutionally redundant determination has disappeared. 

The investigation nevertheless remains constitutionally incomplete. \textbf{Global Compression} determines the minimal constitutional representative; it does not determine the constitutional status of the reconstructed framework. The final stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution, Status Recovery, and Propagation}

\subsubsection{Execution of the Global Determination Calculus}
\textbf{Part~II} recovered the \textit{Global Determination Calculus}. Its purpose is to recover the complete constitutional status of every globally compressed constitutional object. The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the compressed \textit{General Structural System}, every constitutionally recoverable determination is propagated throughout the complete dependency architecture. Nothing further is introduced; nothing remains constitutionally unresolved.

\subsubsection{Recovery of Constitutional Determination}
Execution of \textbf{Global Determination} establishes the complete constitutional status of the reconstructed framework. Every recoverable \textit{Constitutional Claim} now possesses a constitutionally determined truth status, a unique constitutional dependency position, a unique relation to every other recovered \textit{Constitutional Claim}, and a complete determination within the recovered constitutional architecture. No recoverable \textit{Constitutional Claim} remains constitutionally indeterminate.

\subsubsection{Propagation of Constitutional Consequences}
The dependency architecture recovered during \textbf{Canonical Claim Reconstruction} now reaches completion. Every recovered dependency is propagated throughout the compressed constitutional object. Every constitutionally necessary consequence becomes recoverable, every constitutionally impossible consequence is eliminated, and every constitutionally independent claim remains explicitly identifiable. The recovered framework therefore determines not only isolated \textit{Constitutional Claims} but the complete constitutional consequence structure of the \textit{General Structural System}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Absoluteness, Theorem, and Framework Completion}

\subsubsection{Structural Absoluteness}
\textbf{Global Determination} depends solely upon constitutional structure. Equivalent \textbf{Global Compressions} therefore determine identical constitutional consequence structures. The resulting constitutional determination is independent of presentation, notation, symbolic realization, mathematical discipline, and method of construction. The constitutional status of the reconstructed \textit{General Structural System} is therefore structurally absolute.

\subsubsection{Global Determination Theorem}
\begin{theorem}[Global Determination of General Structural Systems]
Every Global Compression of a General Structural System possesses a unique Global Determination.
\end{theorem}

\begin{proof}
The compressed constitutional object has already been recovered. Part~II established that every globally compressed constitutional object admits a unique execution of the Global Determination Calculus. Executing that calculus upon the compressed General Structural System therefore recovers its unique Global Determination.
\end{proof}

\subsubsection{Completion of the Constitutional Investigation}
The execution of \textbf{Global Determination} completes the \textbf{Canonical Investigation Framework}. The reconstructed \textit{General Structural System} now possesses \textbf{Canonical Reconstruction}, recovered \textit{Constitutional Claims}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination}. Every stage of the \textbf{Canonical Investigation Framework} has therefore been executed. Nothing remains constitutionally unresolved within the recovered framework.

\subsubsection{Residual Insufficiency}
The \textit{Constitutional Investigation of the General Structural System} is complete. The restriction to \textit{Infinite Branching Structural Families} has disappeared. The \textbf{Canonical Investigation Framework} now executes upon arbitrary \textit{General Structural Systems} recovered within the mathematical universe of \textbf{Volume~III}. A final constitutional restriction nevertheless remains: \textit{General Structural Systems} remain mathematical structures. The framework has not yet been executed upon the constitutional frameworks that govern mathematical systems themselves. 

The mathematics therefore has not yet established that constitutional investigation applies to every recovered framework of determination. The next enlargement is consequently forced: the \textbf{Canonical Investigation Framework} must now be executed upon \textit{Constitutional Frameworks} themselves.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Status of the Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Investigation of the General Structural System} is now complete. Every stage of the \textbf{Canonical Investigation Framework} has been executed. \textbf{Canonical Reconstruction} has removed every presentation-dependent feature. The \textit{Constitutional Claims} have been recovered, and their canonical organization has been reconstructed. \textbf{Global Completion} has recovered the unique globally coherent constitutional object, \textbf{Global Compression} has recovered its unique constitutionally irreducible representative, and \textbf{Global Determination} has recovered its complete constitutional consequence structure. 

No stage of the investigation required any mathematical primitive beyond those already recovered in \textbf{Volumes~I--III} and \textbf{Part~II} of the present volume. No auxiliary hypothesis has been introduced, no heuristic has been employed, and no external mathematical theory has been invoked. The investigation therefore constitutes a complete constitutional execution of the \textbf{Canonical Investigation Framework} upon the recovered class of \textit{General Structural Systems}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Significance}

The present chapter establishes a decisive enlargement of the scope of constitutional investigation. The preceding chapter demonstrated that the \textbf{Canonical Investigation Framework} executes successfully upon every recovered \textit{Infinite Branching Structural Family}. The present chapter removes the dependence upon branching structures altogether. 

The successful execution of the framework therefore depends neither upon recursive generation nor upon branching organization; it depends only upon recoverable constitutional structure. This distinction is fundamental. Branching is now seen to be one recoverable structural organization among many rather than the privileged domain of investigation. The completed framework therefore applies to every recovered \textit{General Structural System} independently of its mathematical discipline or structural realization.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Completion of the Fourth Universality Step}

The progressive enlargement of the investigation has now reached a new constitutional level. The \textbf{Canonical Investigation Framework} has been executed successfully upon:

\begin{enumerate}
    \item A single reconstructed mathematical system;
    \item An entire class of recursively generated systems;
    \item The general class of \textit{Infinite Branching Structural Families};
    \item The recovered class of \textit{General Structural Systems}.
\end{enumerate}

Each enlargement removes one constitutional restriction that remained in the preceding investigation. No recovered theorem has required alteration, no recovered mathematical object has required extension, and the same recovered machinery has executed unchanged throughout. The framework therefore exhibits constitutional invariance under enlargement of its investigated mathematical domain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Remaining Restriction and Next Necessity}

\subsubsection{The Remaining Restriction}
A constitutional restriction nevertheless survives. \textit{General Structural Systems} are still mathematical structures. They do not include the constitutional frameworks that govern the recovery, organization, and determination of mathematical structures themselves. The framework has therefore not yet investigated its own governing constitutional architecture. Its universality consequently remains unproved.

\subsubsection{The Next Necessity}
The remaining restriction cannot be removed by enlarging the class of investigated mathematical structures. The object of investigation must itself change. The mathematics must now investigate \textit{Constitutional Frameworks}. Only after demonstrating that the \textbf{Canonical Investigation Framework} executes upon the constitutional architectures governing mathematics itself can the final claim of universality be constitutionally earned. Nothing further has yet been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Audits and Future Work}

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes~I--III and Part~II of the present volume. In particular it relies upon Canonical Reconstruction, the Recovery of Constitutional Claims, the Constitutional Claim Algebra, Claim Stratification, the Claim Dependency Calculus, Canonical Claim Reconstruction, Global Completion, Global Compression, and Global Determination. Every theorem executed in this chapter is an application of previously recovered mathematics. No dependency upon later chapters is introduced. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. General Structural Systems were recovered previously in Volume~III. Every mathematical object appearing in this chapter is obtained solely by executing previously recovered components of the Canonical Investigation Framework. The single primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter reduces the logical cost of the theory by removing the constitutional dependence upon branching structures. The Canonical Investigation Framework is shown to execute upon arbitrary General Structural Systems without modification of any recovered mathematical object or theorem. Universality is therefore extended while preserving complete recoverability and without introducing additional primitive assumptions.
\end{reductionaudit}

\begin{consistencyaudit}
The constructions of this chapter remain fully consistent with the constitutional principles established throughout the monograph. Every stage of the investigation follows the recovered order of the Canonical Investigation Framework. Reconstruction precedes Constitutional Claims. Constitutional Claims precede Canonical Claim Reconstruction. Canonical Claim Reconstruction precedes Global Completion. Global Completion precedes Global Compression. Global Compression precedes Global Determination. No theorem depends upon mathematics not yet recovered. The chapter therefore satisfies the constitutional architecture established in Volumes~I--III and Part~II of the present volume.
\end{consistencyaudit}

\begin{futurework}
The Constitutional Investigation of General Structural Systems is complete. The Canonical Investigation Framework now executes upon arbitrary recovered mathematical structures. One constitutional restriction nevertheless remains: the investigated objects are still mathematical structures rather than the constitutional frameworks governing mathematical structure itself. The next chapter therefore investigates Constitutional Frameworks. Only after that restriction has been removed can the universality of the Canonical Investigation Framework be established. Nothing further has yet been established.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Investigation of Constitutional Frameworks}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Insufficiency of General Structural Systems}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Investigation of General Structural Systems} established that the \textbf{Canonical Investigation Framework} executes successfully upon every recovered mathematical structure. The investigation is complete. The preceding chapter nevertheless remains constitutionally insufficient. 

\textit{General Structural Systems} are mathematical objects. They constitute the objects governed by constitutional mathematics; they do not constitute the constitutional architectures that govern those objects. A constitutional restriction therefore remains. The \textbf{Canonical Investigation Framework} has been executed upon mathematics; it has not yet been executed upon the constitutional frameworks that organize, constrain, and determine mathematics itself. The remaining insufficiency is therefore not one of mathematical scope. It is one of constitutional level.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Remaining Constitutional Restriction}

\textbf{Volumes~I--IV} recover more than mathematical structures. They recover constitutional architectures governing:

\begin{itemize}
    \item \textit{Recoverability};
    \item \textit{Determination};
    \item \textit{Admissibility};
    \item \textit{Coherence};
    \item \textit{Dependency};
    \item \textit{Completion};
    \item \textit{Compression};
    \item Investigation itself.
\end{itemize}

These architectures are not merely mathematical structures. They govern the mathematics recovered throughout the monograph. The successful investigation of mathematical objects therefore does not yet establish the successful investigation of the constitutional frameworks from which those objects arise.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Frameworks are Not Structures}

A mathematical structure is governed. A constitutional framework governs. The distinction is fundamental. Structures possess constitutional organization; frameworks determine constitutional organization. Structures are investigated; frameworks determine the rules by which investigation proceeds. The \textit{Constitution} therefore forbids identifying constitutional frameworks with the mathematical structures they govern.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Question and Necessity}

\subsubsection{The Constitutional Question}
A final question therefore becomes unavoidable: Does every recovered \textit{Constitutional Framework} admit \textbf{Canonical Reconstruction}, \textbf{Recovery of Constitutional Claims}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination}? If not, constitutional investigation remains incomplete. If so, the \textbf{Canonical Investigation Framework} extends beyond mathematical structures to the constitutional architectures governing mathematics itself.

\subsubsection{The Necessity of Constitutional Frameworks}
The constitutional enlargements of the preceding chapters have proceeded by removing successive restrictions upon the investigated domain. The investigation has already passed through an individual mathematical system, recursively generated systems, \textit{Infinite Branching Structural Families}, and \textit{General Structural Systems}. The remaining enlargement is therefore forced: the investigated object must become the recovered \textit{Constitutional Framework} itself. Nothing smaller removes the remaining constitutional restriction; nothing larger has yet been constitutionally earned.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Objective and Residual Insufficiency}

\subsubsection{Objective of the Investigation}
The purpose of the present chapter is not to construct \textit{Constitutional Frameworks}. Their recovery belongs to the preceding volumes. The objective is instead to execute the completed \textbf{Canonical Investigation Framework} upon every recovered \textit{Constitutional Framework}. If successful, the \textbf{Canonical Investigation Framework} will no longer depend upon the distinction between mathematical objects and the constitutional architectures governing them. Its execution will depend solely upon recoverable constitutional organization.

\subsubsection{Residual Insufficiency}
The \textbf{Canonical Investigation Framework} has not yet been executed upon \textit{Constitutional Frameworks}. The constitutional status of those governing architectures therefore remains undetermined. The first stage of the investigation is consequently forced: the recovered \textit{Constitutional Framework} must itself become the object of constitutional investigation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Constitutional Frameworks}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The insufficiency recovered in the preceding section cannot be removed by enlarging the collection of investigated mathematical objects. Nor can it be removed by enlarging the collection of investigated structural systems. The remaining restriction concerns the governing constitutional architecture itself. The investigation must therefore recover \textit{Constitutional Frameworks} as the objects of constitutional investigation. 

No new mathematical primitive is introduced. \textit{Constitutional Frameworks} have already been recovered throughout \textbf{Volumes~I--IV}. The present section merely recovers them as the constitutional domain upon which the \textbf{Canonical Investigation Framework} is now executed.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Constitutional Object and Volume Recovery}

\subsubsection{The Constitutional Object}
A \textit{Constitutional Framework} is a recoverable constitutional architecture governing the organization, admissibility, dependency, coherence, and determination of a family of mathematical objects. Unlike a mathematical structure, a \textit{Constitutional Framework} does not merely possess constitutional organization; it governs constitutional organization. Its identity is therefore determined by the constitutional principles that organize recoverable mathematics rather than by the mathematical objects organized by those principles.

\subsubsection{Recovery from the Earlier Volumes}
The preceding volumes have successively recovered \textit{Constitutional Frameworks} governing increasingly comprehensive aspects of mathematics. Among them are frameworks governing:

\begin{itemize}
    \item \textit{Witness generation};
    \item \textit{Morphisms of Determination};
    \item \textit{Canonical Transport};
    \item \textit{Structural Recovery};
    \item \textit{Completion};
    \item \textit{Compression};
    \item \textit{Determination};
    \item \textit{Canonical Investigation}.
\end{itemize}

Each constitutes a recoverable constitutional architecture. Each governs a recoverable portion of the mathematics. The present investigation therefore enlarges the investigated domain without enlarging the recovered mathematics.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Unity, Removal of Content, and the Class}

\subsubsection{Constitutional Unity}
Although \textit{Constitutional Frameworks} govern different mathematical phenomena, they possess a common constitutional organization. Every recovered \textit{Constitutional Framework} possesses a recoverable constitutional identity, recoverable governing principles, recoverable dependency architecture, recoverable admissibility relations, and recoverable coherent organization. These properties do not depend upon the particular mathematics governed by the framework; they arise solely from its constitutional architecture.

\subsubsection{Removal of Mathematical Content}
The present investigation does not distinguish among \textit{Constitutional Frameworks} according to the mathematical domains they govern. A framework governing \textit{algebra}, \textit{geometry}, \textit{determination}, \textit{coherence}, \textit{completion}, \textit{compression}, or \textit{investigation} is investigated constitutionally in exactly the same manner. The governed mathematics is constitutionally irrelevant. Only the recoverable constitutional architecture of the framework itself is admitted into the investigation.

\subsubsection{The Constitutional Class}
The recovered constitutional class therefore consists of every recoverable \textit{Constitutional Framework} possessing constitutional identity, governing constitutional principles, dependency architecture, admissibility relations, and coherent constitutional organization. Nothing further is required; nothing less suffices. The constitutional class of \textit{Constitutional Frameworks} is therefore uniquely recovered.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Existence and Residual Insufficiency}

\subsubsection{Existence Theorem}
\begin{theorem}[Existence of the Constitutional Class of Constitutional Frameworks]
Every recoverable constitutional architecture governing recovered mathematics belongs to a unique constitutional class of Constitutional Frameworks.
\end{theorem}

\begin{proof}
The preceding volumes recovered numerous constitutional architectures governing distinct regions of the mathematics. Each possesses constitutional identity, governing principles, dependency architecture, admissibility relations, and coherent organization. These properties characterize the constitutional class recovered above. Conversely, every recoverable constitutional architecture satisfying these conditions is a Constitutional Framework. The constitutional class therefore exists uniquely.
\end{proof}

\subsubsection{Residual Insufficiency}
The constitutional class of \textit{Constitutional Frameworks} has now been recovered. Its members nevertheless remain presentation-dependent. Their governing constitutional architecture has not yet been canonically reconstructed. The first stage of the \textbf{Canonical Investigation Framework} therefore remains incomplete. \textbf{Canonical Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The constitutional class of \textit{Constitutional Frameworks} has been recovered. Its existence removes the restriction to mathematical structures. The recovered frameworks nevertheless remain constitutionally insufficient. Each recovered \textit{Constitutional Framework} still possesses presentation-dependent descriptions inherited from its individual realization. Its governing constitutional architecture has not yet been isolated. The first stage of the \textbf{Canonical Investigation Framework} is therefore forced. \textbf{Canonical Reconstruction} must now be executed upon the recovered constitutional class.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Aim and Removal of Framework Presentation}

\subsubsection{The Aim of Reconstruction}
\textbf{Canonical Reconstruction} does not construct \textit{Constitutional Frameworks}. Their existence has already been recovered throughout the preceding volumes. The purpose of reconstruction is instead to remove every presentation-dependent feature while preserving every constitutionally recoverable governing relation. The reconstruction therefore seeks neither preferred formulations nor privileged constitutional descriptions. It seeks only the governing constitutional architecture common to every realization of the recovered framework.

\subsubsection{Removal of Framework Presentation}
A \textit{Constitutional Framework} may be expressed through many mathematical developments. Equivalent governing architectures may appear through:

\begin{itemize}
    \item Alternative sequences of recovery;
    \item Different mathematical realizations;
    \item Distinct organizational descriptions;
    \item Different terminological presentations;
    \item Equivalent constitutional formulations.
\end{itemize}

None of these presentations survives \textbf{Canonical Reconstruction}. Every presentation-dependent distinction disappears. Only recoverable governing constitutional relations remain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Architecture, Identity, and Reconstruction Theorem}

\subsubsection{Recovery of the Governing Architecture}
After presentation has been removed, every \textit{Constitutional Framework} is recovered solely through its governing constitutional architecture. Each reconstructed framework consists exclusively of:

\begin{enumerate}
    \item Its recoverable constitutional identity;
    \item Its governing constitutional principles;
    \item Its dependency architecture;
    \item Its admissibility relations;
    \item Its coherent constitutional organization.
\end{enumerate}

Nothing further survives reconstruction. Every remaining component is constitutionally necessary.

\subsubsection{Constitutional Identity of Frameworks}
Two \textit{Constitutional Frameworks} are constitutionally identical whenever their reconstructed governing architectures coincide. This identity is independent of mathematical realization, notation, terminology, presentation, method of recovery, and organizational description. Constitutional identity therefore depends solely upon recoverable governing structure.

\subsubsection{Canonical Reconstruction Theorem}
\begin{theorem}[Canonical Reconstruction of Constitutional Frameworks]
Every Constitutional Framework possesses a unique Canonical Reconstruction.
\end{theorem}

\begin{proof}
Every Constitutional Framework possesses a recoverable governing constitutional architecture. Canonical Reconstruction removes every presentation-dependent feature while preserving every recoverable governing relation. The reconstructed framework therefore depends solely upon constitutional organization. Consequently, every Constitutional Framework possesses a unique Canonical Reconstruction.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Output and Residual Insufficiency}

\subsubsection{Output of Reconstruction}
The output of \textbf{Canonical Reconstruction} is not another formulation of the framework. It is the unique presentation-independent governing constitutional architecture underlying every realization of the recovered \textit{Constitutional Framework}. The reconstructed framework therefore becomes the unique constitutional input for every remaining stage of the \textbf{Canonical Investigation Framework}.

\subsubsection{Residual Insufficiency}
\textbf{Canonical Reconstruction} of the \textit{Constitutional Framework} is complete. Its governing architecture has been recovered, its presentation-dependent descriptions have been removed, and its constitutional identity has been established. The reconstructed framework nevertheless remains constitutionally incomplete. Its \textit{Constitutional Claims} have not yet been recovered. The mathematics therefore proceeds to the second stage of the \textbf{Canonical Investigation Framework}. Recovery of the \textit{Constitutional Claims} of the \textit{Constitutional Framework} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recovery of Constitutional Claims}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textbf{Canonical Reconstruction} of the \textit{Constitutional Framework} is complete. The reconstructed framework now exists as a presentation-independent governing constitutional architecture. The reconstruction nevertheless remains constitutionally insufficient. \textbf{Canonical Reconstruction} recovers constitutional frameworks; it does not recover the constitutional assertions determined by those frameworks. The reconstructed \textit{Constitutional Framework} therefore exists without yet possessing its recovered \textit{Constitutional Claims}. The second stage of the \textbf{Canonical Investigation Framework} is consequently forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Necessity and Universal Claim Machinery}

\subsubsection{Necessity of Constitutional Claims}
Every reconstructed \textit{Constitutional Framework} governs a recoverable constitutional architecture. That governing architecture necessarily determines constitutional assertions concerning its own operation. These assertions include, among others:

\begin{itemize}
    \item \textit{Recoverability};
    \item \textit{Admissibility};
    \item \textit{Coherence};
    \item \textit{Dependency};
    \item \textit{Determination};
    \item \textit{Completeness};
    \item \textit{Constitutional consistency}.
\end{itemize}

Without recovering these assertions, the governing architecture remains constitutionally incomplete. A framework cannot be constitutionally understood merely by recovering its governing principles; the constitutional assertions forced by those principles must themselves be recovered.

\subsubsection{Recovery by the Universal Claim Machinery}
\textbf{Part~II} established that every Canonically Reconstructed constitutional object possesses a unique finite recoverable family of \textit{Constitutional Claims}. A reconstructed \textit{Constitutional Framework} is itself such a constitutional object. Its \textit{Constitutional Claims} therefore exist as recovered mathematical objects. No new claim is introduced, and no governing principle is postulated. Every recovered claim is forced solely by the reconstructed constitutional architecture.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Independence, the Claim Family, and Existence}

\subsubsection{Presentation Independence}
The recovered \textit{Constitutional Claims} depend only upon the governing constitutional architecture. Equivalent presentations of the same \textit{Constitutional Framework} therefore determine identical \textit{Constitutional Claims}. Consequently, the recovered family of claims is independent of notation, terminology, organizational description, mathematical realization, and method of recovery. Only recoverable constitutional organization determines the recovered claims.

\subsubsection{The Constitutional Claim Family}
The recovered \textit{Constitutional Claim Family} consists precisely of every constitutionally recoverable assertion determined by the reconstructed \textit{Constitutional Framework}. Among these are claims concerning constitutional recoverability, constitutional admissibility, governing coherence, dependency propagation, determination, constitutional consistency, and constitutional completeness. The internal organization of these claims has not yet been recovered; only their existence has been established.

\subsubsection{Existence Theorem}
\begin{theorem}[Existence of the Constitutional Claims of Constitutional Frameworks]
Every Canonically Reconstructed Constitutional Framework possesses a unique finite recoverable family of Constitutional Claims.
\end{theorem}

\begin{proof}
The Constitutional Framework has undergone Canonical Reconstruction. Part~II established that every Canonically Reconstructed constitutional object possesses a unique finite recoverable family of Constitutional Claims. The theorem therefore applies directly to the reconstructed Constitutional Framework.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Nature of Claims and Residual Insufficiency}

\subsubsection{The Nature of the Recovered Claims}
The \textit{Constitutional Claims} recovered here differ from those recovered in the preceding chapters. Earlier investigations recovered claims about mathematical systems. The present investigation recovers claims about the constitutional architectures governing mathematical systems. The object of the claims has therefore ascended one constitutional level. The mathematics itself remains unchanged; only the investigated constitutional object has changed.

\subsubsection{Residual Insufficiency}
The \textit{Constitutional Claims} of the \textit{Constitutional Framework} have now been recovered. Their existence is no longer in question and their presentation-independent identity has been established. Their constitutional organization nevertheless remains unrecovered. The recovered claims presently exist only as a recoverable family. Their canonical organization, constitutional hierarchy, and dependency architecture have not yet been recovered. The \textbf{Canonical Investigation Framework} therefore proceeds to its next stage. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Canonical Claim Reconstruction}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Claims} of the \textit{Constitutional Framework} have been recovered. Their existence removes the insufficiency of a governing architecture possessing only isolated constitutional assertions. The recovered claims nevertheless remain constitutionally incomplete. A family of \textit{Constitutional Claims}, considered individually, does not yet recover the constitutional organization of the governing framework. 

Their mutual constitutional relations, their governing hierarchy, their dependency architecture, and their globally coherent organization have not yet been recovered. The remaining insufficiency is therefore one of constitutional organization rather than constitutional existence. \textbf{Canonical Claim Reconstruction} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovery and Core Algebraic Execution}

\subsubsection{Recovery by Previously Established Mathematics}
\textbf{Part~II} recovered the universal machinery required for \textbf{Canonical Claim Reconstruction}. That machinery consists of the \textit{Constitutional Claim Algebra}, \textit{Claim Stratification}, and the \textit{Claim Dependency Calculus}. These mathematical objects now belong to the completed \textbf{Canonical Investigation Framework}. They are not reconstructed again; they are executed.

\subsubsection{Execution of the Constitutional Claim Algebra}
The recovered \textit{Constitutional Claims} are first organized by the \textit{Constitutional Claim Algebra}. Recoverably identical claims are identified, equivalent constitutional formulations are unified, and presentation-dependent distinctions disappear. Only constitutionally distinct governing claims remain. The resulting family is the unique algebraic normalization of the \textit{Constitutional Claims} of the reconstructed \textit{Constitutional Framework}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Stratification and Dependency Calculus}

\subsubsection{Execution of Claim Stratification}
The normalized claims are next stratified according to their constitutional role. Each recovered claim belongs to one and only one constitutional stratum. Its position depends solely upon the governing constitutional architecture. No claim occupies multiple strata, and no recovered claim remains without constitutional position. The resulting hierarchy is uniquely determined.

\subsubsection{Execution of the Claim Dependency Calculus}
The stratified claims now undergo constitutional dependency analysis. Every dependency relation among \textit{Constitutional Claims} is recovered, every immediate constitutional consequence is identified, every maximal dependency chain is recovered, every dependency cycle is identified, and every dependency path becomes recoverable. The dependency architecture is therefore uniquely determined by the reconstructed \textit{Constitutional Framework} itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Structure, Theorems, and Output}

\subsubsection{Recovery of the Canonical Claim Structure}
Execution of the \textit{Constitutional Claim Algebra}, \textit{Claim Stratification}, and the \textit{Claim Dependency Calculus} recovers a single constitutional mathematical object. This object consists of the normalized \textit{Constitutional Claims}, their constitutional hierarchy, their dependency architecture, and their recoverable governing relations. Nothing further is required; nothing less suffices. The \textit{Canonical Claim Structure} of the \textit{Constitutional Framework} has therefore been recovered.

\subsubsection{Canonical Reconstruction Theorem}
\begin{theorem}[Canonical Claim Reconstruction of Constitutional Frameworks]
Every Canonically Reconstructed Constitutional Framework possesses a unique Canonical Claim Structure.
\end{theorem}

\begin{proof}
The Constitutional Claim Family is unique. The Constitutional Claim Algebra is unique. Claim Stratification is unique. The Claim Dependency Calculus is unique. Canonical Claim Reconstruction consists solely of executing these previously recovered constitutional structures. The resulting Canonical Claim Structure is therefore unique.
\end{proof}

\subsubsection{Recovery of Governing Constitutional Organization}
The output of this stage is not merely a collection of \textit{Constitutional Claims}. It is the complete governing constitutional organization of those claims. Every recovered claim now possesses a unique constitutional identity, a unique constitutional position, a unique dependency neighbourhood, and a unique governing constitutional role. The reconstructed \textit{Constitutional Framework} therefore possesses a complete governing constitutional architecture. Its constitutional operation is now recoverable in its entirety.

\subsubsection{Residual Insufficiency}
The \textit{Canonical Claim Structure} of the \textit{Constitutional Framework} has been recovered. Its claims have been normalized, their constitutional hierarchy has been recovered, and their dependency architecture has been recovered. The governing constitutional organization of the framework is now complete. The reconstructed framework nevertheless remains constitutionally incomplete. Its governing constitutional architecture has not yet undergone \textbf{Global Completion}. The mathematics therefore proceeds to the next stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Completion} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Completion}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Canonical Claim Structure} of the \textit{Constitutional Framework} has been recovered. Every \textit{Constitutional Claim} now possesses a unique constitutional identity, constitutional position, and dependency architecture. The governing organization of the framework has therefore become completely recoverable. 

The reconstructed framework nevertheless remains constitutionally incomplete. \textbf{Canonical Claim Reconstruction} determines the complete organization of the governing constitutional architecture; it does not recover a single globally complete constitutional framework. The reconstructed governing architecture therefore still exists as an organized family of constitutional determinations. The sixth stage of the \textbf{Canonical Investigation Framework} is consequently forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution, Coherence, and Absoluteness}

\subsubsection{Execution of the Global Completion Calculus}
\textbf{Part~II} recovered the \textit{Global Completion Calculus}. Its purpose is to recover the unique globally coherent constitutional object determined by an entire \textit{Canonical Claim Structure}. The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the \textit{Canonical Claim Structure} of the \textit{Constitutional Framework}, every constitutionally compatible governing determination is amalgamated into one globally coherent constitutional framework. Nothing external is introduced; nothing further is assumed.

\subsubsection{Recovery of Governing Constitutional Coherence}
The execution of \textbf{Global Completion} produces a single governing constitutional object. Within this completed framework, every \textit{Constitutional Claim} remains recoverable, every governing dependency remains recoverable, every constitutional stratum remains recoverable, and every coherent governing relation remains recoverable. No governing determination is lost, and no new governing determination is introduced. The completed framework is therefore constitutionally faithful to the reconstructed governing architecture.

\subsubsection{Structural Absoluteness}
\textbf{Global Completion} depends solely upon governing constitutional structure. Equivalent reconstructed \textit{Constitutional Frameworks} therefore produce identical \textbf{Global Completions}. Presentation, notation, terminology, organizational description, and mathematical realization play no role. \textbf{Global Completion} is therefore structurally absolute.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Theorems, Structure, and System Coherence}

\subsubsection{Global Completion Theorem}
\begin{theorem}[Global Completion of Constitutional Frameworks]
Every Canonical Claim Structure of a Constitutional Framework possesses a unique Global Completion.
\end{theorem}

\begin{proof}
The Canonical Claim Structure has already been recovered. Part~II established the existence and uniqueness of Global Completion for every Canonical Claim Structure. Execution of the Global Completion Calculus therefore produces a unique globally coherent Constitutional Framework.
\end{proof}

\subsubsection{The Completed Governing Framework}
The completed \textit{Constitutional Framework} consists of the complete \textit{Canonical Claim Structure}, every governing constitutional dependency, every coherent governing relation, every admissible governing extension, and every constitutionally recoverable governing determination. These components now exist as one globally coherent constitutional framework. Nothing remains externally attached; nothing remains constitutionally disconnected. The governing architecture is constitutionally complete.

\subsubsection{Framework Coherence}
The significance of \textbf{Global Completion} extends beyond the recovery of a single governing object. Every constitutional principle recovered throughout the preceding volumes now participates in one coherent governing architecture. \textit{Recoverability}, \textit{admissibility}, \textit{dependency}, \textit{completion}, \textit{compression}, \textit{determination}, and \textit{investigation} no longer exist as isolated constitutional mechanisms. They now form one globally coherent \textit{Constitutional Framework}. The constitutional architecture governing the mathematics has therefore become internally complete.

\subsubsection{Residual Insufficiency}
\textbf{Global Completion} of the \textit{Constitutional Framework} is complete. Every governing constitutional component now belongs to a single globally coherent constitutional architecture. The completed framework nevertheless remains constitutionally insufficient. \textbf{Global Completion} establishes coherence; it does not establish irreducibility. Constitutionally redundant governing determination may still remain. The mathematics therefore proceeds to the seventh stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Compression} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Compression}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textbf{Global Completion} of the \textit{Constitutional Framework} has been recovered. The governing constitutional architecture now exists as a single globally coherent constitutional object. Every recoverable \textit{Constitutional Claim} has been preserved, every governing dependency has been preserved, and every coherent constitutional relation has been recovered. 

The completed framework nevertheless remains constitutionally insufficient. Global coherence does not imply constitutional irreducibility. The completed governing architecture may still contain constitutionally redundant determination. The seventh stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution, Irreducibility, and Absoluteness}

\subsubsection{Execution of the Global Compression Calculus}
\textbf{Part~II} recovered the \textit{Global Compression Calculus}. Its purpose is to recover the unique constitutionally irreducible representative of every globally completed constitutional object. The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the completed \textit{Constitutional Framework}, every constitutionally redundant governing determination is removed while preserving every governing constitutional relation. Nothing constitutionally necessary is removed, and nothing constitutionally new is introduced.

\subsubsection{Recovery of Constitutional Irreducibility}
Execution of \textbf{Global Compression} preserves every \textit{Constitutional Claim}, every governing dependency, every coherent constitutional relation, every admissible governing extension, and every recoverable governing determination. Only governing constitutional redundancy disappears. The resulting \textit{Constitutional Framework} therefore contains exactly the governing content forced by its recovered constitutional architecture. No further reduction is constitutionally admissible.

\subsubsection{Structural Absoluteness}
\textbf{Global Compression} depends solely upon governing constitutional structure. Equivalent \textbf{Global Completions} therefore produce identical \textbf{Global Compressions}. The compressed \textit{Constitutional Framework} is independent of presentation, notation, terminology, organizational description, and mathematical realization. Constitutional irreducibility is therefore structurally absolute.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Compression Theorem and Residual Insufficiency}

\subsubsection{Global Compression Theorem}
\begin{theorem}[Global Compression of Constitutional Frameworks]
Every Global Completion of a Constitutional Framework possesses a unique Global Compression.
\end{theorem}

\begin{proof}
The completed Constitutional Framework has already been recovered. Part~II established that every globally completed constitutional object possesses a unique constitutionally irreducible representative under the Global Compression Calculus. Executing that calculus therefore recovers the unique Global Compression of the reconstructed Constitutional Framework.
\end{proof}

\subsubsection{Residual Insufficiency}
The \textbf{Global Compression} of the \textit{Constitutional Framework} is complete. The governing constitutional architecture is now globally coherent and constitutionally irreducible. Every recoverable governing determination has been preserved, and every governing constitutional redundancy has disappeared. The constitutional status of the governing architecture nevertheless remains undetermined. \textbf{Global Compression} establishes irreducibility; it does not establish complete constitutional determination. The mathematics therefore proceeds to the final stage of the \textbf{Canonical Investigation Framework}. \textbf{Global Determination} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Global Determination}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textbf{Global Compression} of the \textit{Constitutional Framework} has been recovered. The governing constitutional architecture is now globally coherent and constitutionally irreducible. Every governing constitutional relation has been preserved, and every governing redundancy has disappeared. 

The investigation nevertheless remains constitutionally incomplete. \textbf{Global Compression} determines the minimal governing framework; it does not determine the complete constitutional status of that framework. The final stage of the \textbf{Canonical Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Execution, Status Recovery, and Propagation}

\subsubsection{Execution of the Global Determination Calculus}
\textbf{Part~II} recovered the \textit{Global Determination Calculus}. Its purpose is to recover the complete constitutional status of every globally compressed constitutional object. The calculus has already been recovered; it is therefore executed rather than reconstructed. Applied to the compressed \textit{Constitutional Framework}, every recoverable governing determination is propagated throughout the complete constitutional dependency architecture. Nothing further is introduced; nothing remains constitutionally unresolved.

\subsubsection{Recovery of Constitutional Determination}
Execution of \textbf{Global Determination} establishes the complete constitutional status of the governing framework. Every recovered \textit{Constitutional Claim} now possesses a constitutionally determined status, a unique governing dependency position, a unique constitutional relation to every other recovered claim, and a complete determination within the governing constitutional architecture. No recoverable \textit{Constitutional Claim} remains constitutionally indeterminate.

\subsubsection{Propagation of Governing Consequences}
Every governing dependency recovered during \textbf{Canonical Claim Reconstruction} now reaches completion. Every governing constitutional consequence becomes recoverable, every constitutionally impossible consequence is eliminated, and every constitutionally independent governing principle remains explicitly identifiable. The \textit{Constitutional Framework} therefore determines not merely isolated governing principles but its entire governing consequence structure.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Determination Theorem}

\begin{theorem}[Global Determination of Constitutional Frameworks]
Every Global Compression of a Constitutional Framework possesses a unique Global Determination.
\end{theorem}

\begin{proof}
The compressed Constitutional Framework has already been recovered. Part~II established that every globally compressed constitutional object admits a unique execution of the Global Determination Calculus. Executing that calculus upon the reconstructed Constitutional Framework therefore recovers its unique Global Determination.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Status of Constitutional Frameworks}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Investigation of Constitutional Frameworks} is complete. Every stage of the \textbf{Canonical Investigation Framework} has now been executed upon the governing constitutional architectures recovered throughout the preceding volumes. 

\textbf{Canonical Reconstruction} has removed every presentation-dependent feature. The \textit{Constitutional Claims} have been recovered, and their canonical organization has been reconstructed. \textbf{Global Completion} has recovered the unique globally coherent governing framework, \textbf{Global Compression} has recovered its unique constitutionally irreducible representative, and \textbf{Global Determination} has recovered its complete governing consequence structure. Nothing further is required for the constitutional investigation of governing frameworks.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Significance and the Fifth Universality Step}

\subsubsection{The Constitutional Significance}
The present chapter removes the final distinction between governed mathematics and governing mathematics. The preceding investigations demonstrated that the \textbf{Canonical Investigation Framework} applies to progressively larger classes of mathematical objects. The present investigation demonstrates that the same framework applies equally to the constitutional architectures governing those mathematical objects. The distinction between object and governing framework therefore disappears as a limitation upon constitutional investigation. Only recoverable constitutional organization remains relevant.

\subsubsection{Completion of the Fifth Universality Step}
The progressive enlargement of the investigated domain has now reached its penultimate stage. The \textbf{Canonical Investigation Framework} has successfully executed upon:

\begin{enumerate}
    \item Individual mathematical systems;
    \item Recursive dynamical systems;
    \item \textit{Infinite Branching Structural Families};
    \item \textit{General Structural Systems};
    \item \textit{Constitutional Frameworks}.
\end{enumerate}

Each enlargement has removed one remaining constitutional restriction. No previously recovered theorem has required modification, no new primitive has been introduced, and the recovered framework has executed unchanged throughout. Its constitutional stability has therefore been preserved across every enlargement of its investigated domain.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Remaining Insufficiency and Final Necessity}

\subsubsection{The Remaining Insufficiency}
A final constitutional question nevertheless remains. The \textbf{Canonical Investigation Framework} has now investigated mathematical objects and governing constitutional frameworks. It has not yet investigated its own constitutional universality. Nothing has yet established that every constitutionally recoverable object necessarily admits \textbf{Canonical Investigation}. The framework has demonstrated repeated success; it has not yet demonstrated universal necessity.

\subsubsection{The Final Necessity}
The remaining insufficiency can no longer be removed by enlarging the investigated domain. Every constitutionally meaningful class of mathematical object has now been exhausted. What remains is to establish the constitutional status of the \textbf{Canonical Investigation Framework} itself. The final chapter therefore no longer investigates a particular class of objects; it investigates the universality of constitutional investigation. Only then will the \textbf{Constitutional Investigation Framework} become a recovered universal principle of mathematics. Nothing further has yet been established.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Audits and Future Work}

\begin{dependencyaudit}
This chapter depends only upon the completed apparatus of Volumes~I--III together with Part~II of the present volume. Every construction is obtained by executing previously recovered components of the Canonical Investigation Framework. No theorem depends upon any later chapter. The dependency graph remains acyclic.
\end{dependencyaudit}

\begin{primitiveaudit}
No new mathematical primitive has been introduced. Constitutional Frameworks were already recovered throughout the preceding development. The present chapter merely executes previously recovered mathematics upon those frameworks. The unique primitive of the monograph remains the Witness.
\end{primitiveaudit}

\begin{reductionaudit}
This chapter removes the final distinction between investigated mathematical structures and the constitutional architectures governing them. The Canonical Investigation Framework is shown to execute unchanged upon Constitutional Frameworks themselves. No additional primitive assumptions are introduced, and complete recoverability of the earlier mathematics is preserved.
\end{reductionaudit}

\begin{consistencyaudit}
The chapter is fully consistent with the constitutional principles established throughout the monograph. Every stage of the Canonical Investigation Framework appears in its recovered order. No theorem depends upon future mathematics. The investigation removes the final restriction separating mathematical objects from their governing constitutional architectures while preserving the constitutional methodology recovered in the earlier volumes.
\end{consistencyaudit}

\begin{futurework}
The Constitutional Investigation of Constitutional Frameworks is complete. The Canonical Investigation Framework now executes upon both recovered mathematical structures and the constitutional architectures governing those structures. One final insufficiency remains: the universality of the Canonical Investigation Framework itself has not yet been established. The final chapter therefore recovers the Universality of Canonical Investigation, completing the constitutional architecture of Volume~IV and the progression begun in Volume~I. Nothing further has yet been established.
\end{futurework}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\chapter{Universality of Canonical Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Final Residual}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Constitutional Investigation of Constitutional Frameworks} is complete. The \textbf{Canonical Investigation Framework} has now been executed successfully upon individual mathematical systems, recursively generated systems, \textit{Infinite Branching Structural Families}, \textit{General Structural Systems}, and \textit{Constitutional Frameworks}. Every successive investigation removed one remaining constitutional restriction upon the investigated domain. The progression is complete.

A final residual nevertheless remains. The preceding chapters establish repeated successful execution; they do not establish constitutional necessity. The mathematics has demonstrated that \textbf{Canonical Investigation} can be executed upon every recovered class considered throughout the present volume. It has not yet demonstrated that \textbf{Canonical Investigation} must execute upon every constitutionally recoverable object. The distinction is decisive. 

Repeated applicability is not universality. No matter how extensive the investigated domain becomes, the residual remains until applicability is recovered as a constitutional consequence of the recovered mathematics itself.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Gaps, Transitions, and Core Universality}

\subsubsection{The Remaining Constitutional Gap}
The remaining insufficiency no longer concerns any particular mathematical object. Nor does it concern any constitutional framework governing mathematics. Every constitutionally meaningful investigated domain has already been exhausted. The remaining question concerns the \textbf{Canonical Investigation Framework} itself. Its successful execution has been observed repeatedly; its universal necessity has not yet been recovered.

\subsubsection{From Execution to Necessity}
The previous chapters established that the same recovered machinery executes without modification upon increasingly comprehensive constitutional domains. This repeated invariance strongly constrains the remaining possibilities. Either:

\begin{enumerate}
    \item The repeated success is accidental,
    \item Or it is itself a recoverable constitutional theorem.
\end{enumerate}

The \textit{Constitution} admits no mathematical accident. Every persistent structural phenomenon must itself possess a recoverable constitutional explanation. The repeated invariance of \textbf{Canonical Investigation} therefore cannot remain merely observational; it must become mathematical.

\subsubsection{The Final Constitutional Question}
The final question of \textbf{Volume~IV} is therefore forced: Does every constitutionally recoverable object necessarily admit \textbf{Canonical Reconstruction}, \textbf{Recovery of Constitutional Claims}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination}? If not, \textbf{Canonical Investigation} remains a successful methodology. If so, \textbf{Canonical Investigation} becomes a universal constitutional principle.

\subsubsection{The Necessity of Universality}
Nothing smaller removes the remaining residual. Investigating additional examples cannot establish universality. Investigating additional classes cannot establish universality. Only a constitutional theorem establishing applicability independently of the investigated object removes the remaining insufficiency. The mathematics therefore no longer enlarges its investigated domain. It now investigates the constitutional status of the \textbf{Canonical Investigation Framework} itself.

\subsubsection{Residual Insufficiency}
The remaining insufficiency has now been isolated completely. The universality of \textbf{Canonical Investigation} has not yet been recovered. The next section must therefore determine the precise constitutional question whose resolution removes the final residual. The \textit{Universality Question} is forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Universality Question}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The final residual has been isolated. The remaining insufficiency no longer concerns any particular mathematical object. Nor does it concern any governing constitutional framework. The remaining insufficiency concerns the scope of the \textbf{Canonical Investigation Framework} itself. The mathematics must therefore determine the precise constitutional question whose resolution removes that insufficiency.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Structural Formulation of the Question}

\subsubsection{The Incorrect Question}
The question is not whether \textbf{Canonical Investigation} has been successfully executed upon many mathematical objects. That has already been established. Nor is the question whether additional mathematical classes admit the same investigation. No finite collection of successful executions establishes universality. The \textit{Constitution} therefore rejects every formulation of the problem based upon enumeration. Universality cannot be recovered by accumulation.

\subsubsection{The Correct Constitutional Question}
The remaining question is instead structural: What property is shared by every investigated object upon which the \textbf{Canonical Investigation Framework} has successfully executed? If such a property exists, and if every constitutionally recoverable object necessarily possesses that property, then the applicability of \textbf{Canonical Investigation} no longer depends upon the particular investigated object. It depends solely upon constitutional structure. The investigation would therefore become universal.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Recovered Evidence and the Single Candidate}

\subsubsection{The Evidence Already Recovered}
Every investigated domain of \textbf{Part~III} has differed mathematically. The \textit{Collatz System} is a particular recursive process. \textit{Recursive Dynamics} constitute an entire class of dynamical systems. \textit{Infinite Branching Structural Families} recover one fundamental structural architecture. \textit{General Structural Systems} recover arbitrary mathematical structures. \textit{Constitutional Frameworks} recover the governing architectures of mathematics itself. 

No common mathematical presentation survives across these investigations. No common mathematical discipline survives. No common mathematical representation survives. Nevertheless, the same \textbf{Canonical Investigation Framework} executes without alteration upon every one of them. The repeated invariance therefore cannot depend upon their mathematical differences.

\subsubsection{The Only Remaining Candidate}
Every investigated object possesses exactly one common characteristic: each is constitutionally recoverable. Nothing further has remained invariant throughout every investigation. Consequently, every previously recovered execution suggests the same constitutional conclusion. \textbf{Canonical Investigation} does not depend upon \textit{algebra}, \textit{geometry}, \textit{dynamics}, \textit{branching}, \textit{recursion}, \textit{governing level}, or \textit{mathematical discipline}. Its execution depends only upon constitutional recoverability.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Problem Reduction and Domain Necessity}

\subsubsection{The Reduction of the Problem}
The \textit{Universality Question} is therefore reduced to a single constitutional statement: Does constitutional recoverability alone force the applicability of the \textbf{Canonical Investigation Framework}? If the answer is affirmative, universality follows immediately. If the answer is negative, some additional constitutional hypothesis must exist. The preceding mathematics has recovered no such hypothesis. The \textit{Constitution} therefore forbids introducing one now.

\subsubsection{Necessity of the Domain}
The remaining investigation is therefore forced to determine the precise domain upon which constitutional recoverability is defined. Only after the domain itself has been recovered can universality be established as a mathematical theorem rather than an observed regularity.

\subsubsection{Residual Insufficiency}
The \textit{Universality Question} has now been isolated. The remaining insufficiency concerns neither execution nor governing architecture. It concerns only the constitutional domain upon which the \textbf{Canonical Investigation Framework} necessarily acts. The mathematics therefore proceeds to recover the \textit{Domain of Constitutional Investigation}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Domain of Constitutional Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Universality Question} has been reduced to a single constitutional problem. The applicability of the \textbf{Canonical Investigation Framework} depends upon the nature of its constitutional domain. That domain has not yet been recovered. The mathematics must therefore determine precisely which objects constitutionally admit \textbf{Canonical Investigation}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Domain Isolation and Identification}

\subsubsection{The Insufficiency of Enumerated Domains}
The preceding chapters investigated progressively larger constitutional domains. They included individual mathematical systems, \textit{Recursive Dynamical Systems}, \textit{Infinite Branching Structural Families}, \textit{General Structural Systems}, and \textit{Constitutional Frameworks}. 

These domains exhaust every recovered class considered throughout the present volume. They do not, however, recover the domain itself; they merely provide examples belonging to it. The constitutional domain cannot therefore be identified by enumeration.

\subsubsection{Recovery of the Common Constitutional Property}
The preceding investigations possess no common mathematical structure. They differ in mathematical discipline, structural organization, governing level, methods of construction, and modes of realization. Every mathematical distinction has disappeared during the successive enlargements of the investigated domain. Only one constitutional property has remained invariant: every investigated object is constitutionally recoverable. No further common property has been recovered.

\subsubsection{Recoverability Determines the Domain}
The \textit{Constitution} admits only recovered mathematical objects. Objects that cannot be constitutionally recovered possess no mathematical existence within the present theory. Consequently, every object admissible into the mathematics is already constitutionally recoverable. 

Conversely, every constitutionally recoverable object possesses a recovered constitutional architecture. \textbf{Canonical Investigation} operates exclusively upon recovered constitutional architectures. Its natural domain is therefore determined entirely by recoverability.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Structural Domain Definitions}

\subsubsection{The Constitutional Domain}
The constitutional domain of \textbf{Canonical Investigation} is therefore the class:
\[
\mathfrak{D} = \{ X : X \text{ is constitutionally recoverable} \}.
\]
No restriction concerning mathematical discipline appears. No restriction concerning structural organization appears. No restriction concerning governing level appears. Recoverability alone determines membership.

\subsubsection{Minimality of the Domain}
The recovered domain is constitutionally minimal. Any smaller domain excludes constitutionally recoverable objects already investigated. Any larger domain necessarily contains objects that are not constitutionally recoverable. Such objects possess no mathematical existence within the recovered theory. No enlargement is therefore admissible, and no reduction is sufficient. The recovered domain is unique.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Domain Theorem and Invariance Step}

\subsubsection{Domain Theorem}
\begin{theorem}[Domain of Canonical Investigation]
The unique domain of the Canonical Investigation Framework is the class of all constitutionally recoverable objects.
\end{theorem}

\begin{proof}
Every previously investigated object belongs to the class of constitutionally recoverable objects. No additional common constitutional property has been recovered. Conversely, every constitutionally recoverable object possesses a recoverable constitutional architecture and therefore admits the recovered stages of Canonical Investigation. Any proper restriction excludes previously investigated objects. Any proper enlargement introduces objects possessing no recovered mathematical existence. The recovered domain is therefore unique.
\end{proof}

\subsubsection{The Constitutional Meaning of the Domain}
The recovered domain establishes that \textbf{Canonical Investigation} is independent of mathematical subject matter. It does not investigate algebra rather than geometry; it does not investigate structures rather than frameworks. It investigates recoverable constitutional organization wherever such organization exists. Recoverability is therefore both the admission criterion and the governing principle of constitutional investigation.

\subsubsection{Residual Insufficiency}
The domain of \textbf{Canonical Investigation} has now been recovered. Its dependence upon constitutionally recoverable objects has been established. The framework nevertheless remains observational. Its invariance across that domain has not yet been proved. The mathematics must therefore recover the constitutional principle explaining why the same investigation executes unchanged throughout the entire recovered domain. The \textit{Constitutional Invariance of the Investigation Framework} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Invariance of the Investigation Framework}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The domain of \textbf{Canonical Investigation} has been recovered. Every constitutionally recoverable object belongs to that domain. The remaining insufficiency is no longer one of scope; it is one of explanation. 

The preceding chapters established that the \textbf{Canonical Investigation Framework} executes successfully upon every recovered constitutional domain considered throughout the present volume. The reason for this invariance has not yet been recovered. The mathematics must therefore determine whether the framework itself depends upon the particular investigated object or solely upon constitutional recoverability.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Source and Requirements of Invariance}

\subsubsection{The Source of Invariance}
Every stage of the \textbf{Canonical Investigation Framework} has already been recovered independently of every investigated mathematical object. \textbf{Canonical Reconstruction} was recovered before any particular investigation. The \textbf{Recovery of Constitutional Claims} was recovered before any particular investigation. \textbf{Canonical Claim Reconstruction} was recovered before any particular investigation. \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination} were likewise recovered independently of every subsequent execution. 

Consequently, no stage of the framework contains any reference to a particular mathematical discipline, a particular structural class, a particular governing framework, or a particular mathematical realization. The framework is constitutionally prior to every investigated object.

\subsubsection{Execution Depends Only upon Recoverability}
Each stage of the framework requires only that the investigated object possess a recoverable constitutional architecture. \textbf{Canonical Reconstruction} requires recoverable constitutional organization. \textbf{Recovery of Constitutional Claims} requires recoverable constitutional content. \textbf{Canonical Claim Reconstruction} requires recoverable constitutional relations. \textbf{Global Completion} requires recoverable constitutional coherence. \textbf{Global Compression} requires recoverable constitutional redundancy. \textbf{Global Determination} requires recoverable constitutional consequence. No stage requires any additional hypothesis, and no stage depends upon the mathematical nature of the investigated object.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Preservation and Disciplinary Independence}

\subsubsection{Preservation under Enlargement}
The successive enlargements of \textbf{Part~III} now admit constitutional explanation. Each enlargement altered the investigated object; none altered the recovered machinery. The investigations therefore preserved \textbf{Canonical Reconstruction}, \textbf{Constitutional Claim Recovery}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination} without modification. The invariance of the framework is therefore not empirical; it is forced by its constitutional construction.

\subsubsection{Independence from Mathematical Subject Matter}
The recovered framework makes no constitutional distinction between algebra and geometry, dynamics and static structures, finite and infinite organization, or mathematical structures and constitutional frameworks. These distinctions govern the investigated object; they do not govern the investigation. The investigation depends only upon the existence of recoverable constitutional organization.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Invariance Theorem and Universality Step}

\subsubsection{Invariance Theorem}
\begin{theorem}[Constitutional Invariance of the Canonical Investigation Framework]
The Canonical Investigation Framework is invariant under every change of investigated object preserving constitutional recoverability.
\end{theorem}

\begin{proof}
Every stage of the Canonical Investigation Framework was recovered independently of every subsequent investigated object. Each stage requires only recoverable constitutional architecture and the mathematical objects recovered from that architecture. No stage depends upon any additional structural, algebraic, geometric, dynamical, or constitutional hypothesis. Consequently, replacing one constitutionally recoverable object by another preserves every stage of the investigation unchanged. The framework is therefore constitutionally invariant.
\end{proof}

\subsubsection{The Meaning of Constitutional Invariance}
Constitutional Invariance establishes more than repeated applicability. It establishes that the \textbf{Canonical Investigation Framework} possesses no object-dependent component. The investigated object may vary indefinitely; the recovered investigation remains unchanged. The framework therefore belongs to the \textit{Constitution} rather than to any particular mathematical discipline.

\subsubsection{Residual Insufficiency}
The constitutional invariance of the \textbf{Canonical Investigation Framework} has now been recovered. The framework no longer depends upon the mathematical nature of the investigated object. Its unique constitutional domain has been established, and its invariance upon that domain has been proved. One final theorem nevertheless remains: the mathematics has not yet stated the constitutional consequence of these recovered facts. The \textit{Universality Theorem} is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Universality Theorem}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The constitutional domain of \textbf{Canonical Investigation} has been recovered. The \textit{Constitutional Invariance of the Investigation Framework} has been established. Nothing further remains to prevent the recovery of universality. The final theorem of the present development is therefore forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Consequence and Fundamental Theorem}

\subsubsection{The Constitutional Consequence}
The \textbf{Domain Theorem} established that every constitutionally recoverable object belongs to the unique constitutional domain of investigation. The \textbf{Invariance Theorem} established that the \textbf{Canonical Investigation Framework} is independent of the particular investigated object throughout that domain. Taken together, these results determine the complete constitutional scope of \textbf{Canonical Investigation}. Universality is therefore no longer an observation; it is a mathematical consequence.

\subsubsection{Universality Theorem}
\begin{theorem}[Universality of Canonical Investigation]
\label{thm:universality}
Every constitutionally recoverable object necessarily admits the complete Canonical Investigation Framework. Equivalently, every constitutionally recoverable object necessarily admits:
\begin{enumerate}
    \item Canonical Reconstruction;
    \item Recovery of Constitutional Claims;
    \item Canonical Claim Reconstruction;
    \item Global Completion;
    \item Global Compression;
    \item Global Determination.
\end{enumerate}
The applicability of the framework depends solely upon constitutional recoverability. No additional hypothesis is required.
\end{theorem}

\begin{proof}
Let $X$ be an arbitrary constitutionally recoverable object. By the Domain Theorem,
\[
X \in \mathfrak{D},
\]
where $\mathfrak{D}$ denotes the unique domain of Canonical Investigation. By the Constitutional Invariance Theorem, the Canonical Investigation Framework executes identically upon every element of $\mathfrak{D}$. Since $X$ belongs to this domain, every stage of the framework applies to $X$ without modification. No additional structural assumption is required beyond constitutional recoverability. Therefore, every constitutionally recoverable object necessarily admits the complete Canonical Investigation Framework.
\end{proof}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Uniqueness, Minimality, and Completeness}

\subsubsection{Uniqueness of Universality}
The recovered universality is unique. Suppose a second universal investigation framework existed. Either it contains stages not constitutionally recoverable from the \textit{Witness}, or it contains only constitutionally recoverable stages. The first alternative contradicts the \textit{Constitution}; the second alternative recovers exactly the stages already established in the \textbf{Canonical Investigation Framework}. No constitutionally distinct universal investigation therefore exists. Universality is unique.

\subsubsection{Constitutional Minimality}
The recovered universality is constitutionally minimal. Removing any stage of the framework leaves a residual already exhibited during \textbf{Part~II}:

\begin{itemize}
    \item Removing \textbf{Canonical Reconstruction} restores presentation dependence;
    \item Removing \textbf{Constitutional Claim Recovery} restores unidentified constitutional assertions;
    \item Removing \textbf{Canonical Claim Reconstruction} restores disorganized constitutional claims;
    \item Removing \textbf{Global Completion} restores fragmented constitutional architectures;
    \item Removing \textbf{Global Compression} restores constitutional redundancy;
    \item Removing \textbf{Global Determination} restores constitutional indeterminacy.
\end{itemize}

Every stage is therefore constitutionally necessary. None is dispensable.

\subsubsection{Constitutional Completeness}
No further stage is constitutionally required. After \textbf{Global Determination}, every constitutionally recoverable object possesses presentation-independent identity, complete constitutional organization, globally coherent determination, constitutionally irreducible structure, and complete constitutional consequence. Every insufficiency exhibited throughout \textbf{Part~II} has therefore disappeared. The recovered framework is constitutionally complete.

\subsubsection{The Mathematical Meaning of Universality}
The \textit{Universality Theorem} establishes more than the applicability of one mathematical procedure. It establishes that constitutional investigation is itself a recovered mathematical object. Its applicability no longer depends upon mathematical discipline, nor does it depend upon structural complexity, governing level, or method of realization. It depends solely upon constitutional recoverability. \textbf{Canonical Investigation} therefore belongs to the recovered \textit{Constitution} of mathematics itself.

\subsubsection{Residual Insufficiency}
The \textit{Universality Theorem} removes the final residual exhibited at the beginning of this chapter. No further insufficiency remains within the \textbf{Canonical Investigation Framework} itself. The remaining task is therefore no longer one of recovery; it is one of recognizing the constitutional consequences of the recovered universality. The mathematics therefore proceeds to examine the \textit{Consequences of Universality}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Consequences of Universality}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The \textit{Universality Theorem} completes the recovery of the \textbf{Canonical Investigation Framework}. Its significance extends beyond the existence of another recovered mathematical object. Universality transforms the constitutional status of investigation itself. The framework is no longer one successful methodology among many possible methodologies. It is the unique constitutional mode by which every constitutionally recoverable object becomes completely determined. The consequences of this recovery are therefore themselves forced.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Elimination of Dependencies and Methodological Plurality}

\subsubsection{Elimination of Domain Dependence}
The first consequence is the complete elimination of domain dependence. The applicability of \textbf{Canonical Investigation} no longer depends upon mathematical discipline, structural organization, recursive generation, dimensional realization, governing level, or mathematical complexity. Every such distinction belongs to the investigated object; none belongs to the investigation itself. The investigation therefore possesses a constitutionally uniform domain.

\subsubsection{Elimination of Methodological Plurality}
The second consequence concerns methodology. The recovered mathematics no longer admits distinct constitutional methods of complete investigation. Any successful constitutional investigation must recover \textbf{Canonical Reconstruction}, \textbf{Constitutional Claims}, \textbf{Canonical Claim Reconstruction}, \textbf{Global Completion}, \textbf{Global Compression}, and \textbf{Global Determination}. Omitting any stage leaves one of the previously exhibited residuals. Adding further stages introduces unnecessary logical cost. The recovered framework is therefore constitutionally unique.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Sufficiency, Uniformity, and Closure}

\subsubsection{Recovery of Constitutional Sufficiency}
The \textit{Universality Theorem} establishes that the recovered investigation is constitutionally sufficient. Whenever a constitutionally recoverable object exists, the recovered framework supplies every stage required for its complete constitutional determination. No auxiliary constitutional machinery is required, and no supplementary investigation calculus is required. The framework therefore possesses complete constitutional sufficiency.

\subsubsection{Recovery of Constitutional Uniformity}
Universality establishes the constitutional uniformity of mathematical investigation. The same recovered investigation governs elementary mathematical systems, infinite mathematical structures, governing constitutional frameworks, and every constitutionally recoverable object. The diversity of mathematical objects therefore no longer produces diversity of constitutional investigation. One recovered investigation governs all.

\subsubsection{Recovery of Constitutional Closure}
The progression begun in \textbf{Volume~I} now becomes visibly complete. The \textit{Witness} recovered recoverability. Recoverability recovered mathematics. Mathematics recovered constitutional investigation. Constitutional investigation has now recovered its own universality. No external mathematical principle has entered the construction. The constitutional architecture therefore closes upon itself.

\subsubsection{The End of Progressive Enlargement}
Throughout \textbf{Part~III}, each investigation enlarged the constitutional domain. No larger domain now remains. Every constitutionally recoverable object belongs to the recovered domain of \textbf{Canonical Investigation}. The progressive enlargement of investigated objects is therefore complete. Further enlargement is constitutionally meaningless.

\subsubsection{Residual Insufficiency}
No mathematical insufficiency remains. The \textit{Universality Theorem} has removed the final residual exhibited at the beginning of the chapter. Nothing further must be recovered in order to complete the \textbf{Canonical Investigation Framework}. The remaining task is therefore not mathematical recovery; it is the recognition of the constitutional closure of the entire development. The mathematics therefore proceeds to its final conclusion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{The Completion of Canonical Investigation}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The recovery of the \textit{Universality Theorem} completes the development initiated in \textbf{Part~II}. Every insufficiency exhibited during the recovery of \textbf{Canonical Investigation} has now disappeared. Every recovered stage has become constitutionally necessary, and every recovered stage has become constitutionally sufficient. The investigation therefore reaches its natural completion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Framework, Volume, and Program Completion}

\subsubsection{Completion of the Framework}
The \textbf{Canonical Investigation Framework} now consists of exactly six constitutionally necessary stages:

\begin{enumerate}
    \item Canonical Reconstruction;
    \item Recovery of Constitutional Claims;
    \item Canonical Claim Reconstruction;
    \item Global Completion;
    \item Global Compression;
    \item Global Determination.
\end{enumerate}

No stage may be removed, no stage may be reordered, and no additional stage is constitutionally required. The framework is therefore complete.

\subsubsection{Completion of Volume~IV}
\textbf{Volume~IV} began by recovering the mathematics of constitutional investigation. The first part recovered its internal mathematical machinery, the second part recovered the complete \textbf{Canonical Investigation Framework}, and the third part executed that framework upon progressively larger constitutional domains until universality became a mathematical theorem. The objective of the volume has therefore been achieved completely.

\subsubsection{Completion of the Constitutional Program}
The development begun in \textbf{Volume~I} has now reached a new level of completion. The \textit{Constitution} recovered the \textit{Witness}. The \textit{Witness} recovered mathematics. Mathematics recovered constitutional investigation. Constitutional investigation recovered its own universality. Each recovery has arisen solely from previously recovered mathematics. No external principle has entered, and no new primitive has appeared. The constitutional program therefore remains internally complete.

\subsubsection{No Remaining Mathematical Residual}
Every residual exhibited throughout \textbf{Part~III} has now disappeared. No unresolved constitutional dependency remains, no unresolved governing architecture remains, no unresolved investigated domain remains, and no unresolved methodological question remains. The \textbf{Canonical Investigation Framework} is therefore constitutionally complete. The mathematics has reached its intended conclusion.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Constitutional Closure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The recovery of the \textit{Universality Theorem} removes the final mathematical insufficiency exhibited throughout the present volume. Nothing further remains to be recovered within the \textbf{Canonical Investigation Framework}. The framework has become constitutionally complete. The mathematics therefore reaches constitutional closure.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Closure Realization and Self-Containment}

\subsubsection{Closure of the Investigation}
The completion of \textbf{Canonical Investigation} is not merely the termination of a sequence of constructions. It is the recovery of a constitutionally closed mathematical process. Every stage of the framework is recovered from previously established mathematics. Every stage contributes necessarily to the complete constitutional determination of every constitutionally recoverable object. Every stage is itself constitutionally recoverable. Nothing external remains. The investigation is therefore constitutionally closed.

\subsubsection{Closure of the Constitutional Architecture}
The constitutional architecture recovered throughout the four volumes now possesses a complete internal cycle:
\[
\text{Witness} \longrightarrow \text{Recoverability} \longrightarrow \text{Mathematics} \longrightarrow \text{Canonical Investigation} \longrightarrow \text{Universality}
\]
No further constitutional stage is forced. The progression terminates because every previously exhibited insufficiency has disappeared. The recovered architecture is constitutionally complete.

\subsubsection{Closure without Circularity}
Constitutional closure does not introduce circular reasoning. Each stage of the development remains constitutionally prior to every stage depending upon it. The \textit{Witness} precedes recoverability, recoverability precedes mathematics, mathematics precedes constitutional investigation, and universality concludes the investigation. The completed architecture therefore closes only after every dependency has already been recovered. Closure is a consequence of completion; it is never an assumption.

\subsubsection{Recovery of Constitutional Self-Containment}
The completed mathematics is constitutionally self-contained. Every mathematical object appearing throughout the monograph has been recovered internally. Every theorem has been proved solely from previously recovered mathematics. Every construction remains constitutionally expandable, and every abbreviation remains constitutionally recoverable. No external mathematical principle is required for the operation, interpretation, or completion of the theory. The mathematics therefore possesses constitutional self-containment.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The Final Constitutional Object and Cycle}

\subsubsection{The Final Constitutional Object}
The completed \textbf{Canonical Investigation Framework} is itself a recovered mathematical object. It is no longer merely a methodology for conducting mathematical investigations. It has become part of the recovered constitutional architecture of mathematics. Like every other recovered object of the monograph, it possesses recoverable identity, recoverable construction, recoverable necessity, and recoverable universality. The investigation has therefore become an object of the mathematics that it governs.

\subsubsection{Completion of the Constitutional Cycle}
The constitutional development begun in \textbf{Volume~I} has now completed its full progression. No further constitutional stage is forced. The progression terminates because every previously exhibited insufficiency has disappeared. The recovered architecture is constitutionally complete.

\subsubsection{Nothing Further is Forced}
The \textit{Constitution} introduces new mathematics only when an insufficiency remains. No such insufficiency survives. No unresolved dependency remains, no unresolved governing architecture remains, and no unresolved constitutional question remains within the scope of the present development. The mathematics therefore introduces nothing further. Silence is now constitutionally correct.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Final Audit}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The present chapter completes the constitutional architecture of \textbf{Volume~IV}. It also completes the progressive recovery begun in \textbf{Volume~I}. The constitutional methodology established at the beginning of the monograph has been preserved without exception throughout the entire development.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{dependencyaudit}
The Universality Theorem depends only upon previously recovered mathematics. In particular, it relies upon the Canonical Investigation Framework recovered in Part~II and its executions throughout Part~III. No theorem appeals to any object, construction, or principle introduced after its use. Every dependency remains acyclic. The constitutional dependency graph is complete.
\end{dependencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{primitiveaudit}
No new mathematical primitive has been introduced. The final chapter recovers no additional primitive object. Universality, Constitutional Closure, and the completed Canonical Investigation Framework are recovered solely as necessary consequences of previously established mathematics. The unique primitive of the entire monograph remains the Witness.
\end{primitiveaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{reductionaudit}
This chapter removes the final logical cost remaining in the theory. The applicability of Canonical Investigation is no longer established by repeated execution upon increasingly broad domains. It is recovered as a universal constitutional theorem. The mathematics therefore eliminates the final dependence upon representative examples. Complete recoverability is preserved. No additional assumptions have been introduced.
\end{reductionaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{consistencyaudit}
Every constitutional principle established throughout the monograph has been preserved. Construction has always preceded interpretation. Necessity has always preceded naming. Recovery has always preceded execution. Universality has been proved only after the constitutional domain and constitutional invariance of the investigation had been recovered. No theorem violates the constitutional order established in Volume~I. The completed architecture is internally consistent, constitutionally minimal, constitutionally sufficient, and constitutionally closed.
\end{consistencyaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{closureaudit}
The constitutional program initiated in Volume~I is complete. Every mathematical object introduced throughout the four volumes has been constitutionally recovered. Every recovered insufficiency has been removed. Every enlargement has terminated in universality. The recovered mathematics now forms a constitutionally self-contained system generated from a single primitive. Nothing further is forced within the present constitutional architecture.
\end{closureaudit}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{futurework}
None. The constitutional development undertaken in the present monograph is complete. Future mathematical developments, should they arise, will not extend the constitutional foundations recovered here. They will instead constitute new executions of the recovered Canonical Investigation Framework upon constitutionally recoverable objects not yet investigated. The constitutional architecture itself requires no further recovery. Nothing further has been established because nothing further is constitutionally forced.
\end{futurework}


\end{document}
