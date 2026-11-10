# PeptideMT scientific capability audit — 2026-11-04

Status: **revision 2: documentary review, controlled source-API probes and
retained-data analysis complete; improvement proposals await disposition**.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Navigation: [design guide](README.md) · [first audit](audit_2026_11_04.md) ·
[active follow-up](pending_proposals/scientific_capability_audit.md).

Revision 2 strengthens the first extension with a finding register, executed
counterexamples, a fixed-pool selection analysis and a narrower decision order.
The [revision-2 evidence](evidence/peptidemt_scientific_audit_2026_11_04_review2.json)
retains the earlier report bytes/hash separately; historical evidence is not
silently replaced. The principal new scientific inference is that neither
selector can recover a joint native-label hit absent from the observed pool.
The next utility question must therefore examine proposal/evaluation coverage,
as well as selection. A reproduced malformed-data diagnostic defect is owned
separately in [#34](https://github.com/uibcdf/peptidemt/issues/34).

## 1. Why extend the first audit?

The first review was useful but incomplete: it mainly assessed modern HydrAMP's
numerical implementation and its consumer boundary. That does not answer whether
PeptideMT is becoming an effective peptide-design library. A correct generator
adapter is necessary for its selected workflow, but is not sufficient for
redesign, optimization, target/function composition or informative experiments.

This extension assesses the library against the investigators' own
[purpose](vision_scope.md), [scientific trajectory](scientific_trajectory.md),
[roadmap](roadmap.md), D09–D35 and the narrower implemented contracts. It does not
reopen the accepted architecture or treat future aspirations as failed current
acceptance tests. Much of the scientific reasoning below is already present in
the design guide; the main gap is executable capabilities and evidence, not a
lack of architectural ideas.

**Assessment:** PeptideMT is a credible, conservative experimental composition
layer for a selected generate–assess–select workflow. It is not yet a general
peptide optimizer or a target-directed design tool. It can become substantially
more scientifically useful by making design questions executable, comparing
procedures fairly, and using evidence to choose subsequent actions. More model
wrappers or a larger internally developed generator alone do not establish that
progress.

## 2. Scope, source identity and evidence strength

Read public APIs and their input/result/selection and provider boundaries,
representative W1 tests, user workflow documentation, scientific specifications,
accepted decisions and retained Macrel/HydrAMP evidence. The
[initial snapshot receipt](evidence/peptidemt_scientific_audit_2026_11_04.json)
records the first extension's source/document hashes and Git base. Revision 2
verifies that all 22 runtime source hashes remain unchanged. The working tree is dirty with
substantial pre-existing local work; the base commit does not identify that work.

No new scientific implementation, dataset acquisition, framework import, model
call, prospective benchmark, training or performance test was performed.
Revision 2 executes five controlled semantic scenarios, two malformed-data
paths and a descriptive analysis of two existing H4 assessments. These use
current source APIs, not a newly qualified installed artifact. Engine imports,
model-array opens, network and subprocess creation are blocked inside the
instrument. Existing qualification retains its historical scope. This is not a line-by-line
security review, full current test-suite certification, public installation
audit, systematic literature review or user study.

Use four distinct judgments: **implemented behavior**, **retained qualification**,
**scientific utility not established**, and **proposed capability**. A feature
may satisfy the first two and still lack the third. A negative computational
result can be useful and complete without wet-lab validation.

## 3. Purpose-to-capability matrix

| Intended purpose | Current implementation/evidence | Main gap and consequence |
| --- | --- | --- |
| Receive peptide proposals without altering their meaning | `SequenceRecord`, occurrence-preserving inputs, MolSysMT FASTA delegation; W1/W3 evidence | Chemistry/context can be stored, but storage does not qualify chemistry-dependent evaluation. |
| Evaluate bioactive functions and adverse effects | Qualified Macrel AMP/hemolysis route and replayable results | One narrow predictive binding, with unresolved calibration/domain coverage; not arbitrary family or assay evaluation. |
| Generate peptides | Exact accepted HydrAMP dev3 route and generation receipt; real adapter evidence | Single selected target-free route. Its numerical fidelity does not measure discovery yield or comparative usefulness. |
| Redesign a supplied peptide | Encoder E2 evidence exists in the provider fork; analogue drafts remain paused | No qualified modern analogue operation or public PeptideMT redesign workflow. Encoder correctness is not redesign effectiveness. |
| Select candidates reproducibly | Two exact D35 lexicographic policies, explicit exclusions and tie rule | No new action-specific feasibility, diversity or uncertainty-aware selector is implemented. Ranking is not satisfaction of a design problem. |
| Optimize exploration using evaluations | Conceptually specified in D27–D32 and the trajectory | No current public adaptive search loop changes subsequent proposals. Selecting a completed pool is not optimization feedback. |
| Combine target engagement with functional properties | Target context can be retained in arbitrary metadata | No qualified target-conditioned/evaluation route. `generate_hydramp(n_target=...)` specifies an output count, not a molecular target. |
| Handle multiple functional families | Rich concept/resource discussion and catalog | No executed CPP/ACP/multi-family workflow; Macrel-specific admission/results are not a general functional evidence contract. |
| Respect molecular chemistry and design restrictions | Conservative rejection of unsupported explicit chemistry, preservation of unknowns | No scoped chemical transformations, protected-position redesign or qualified modified-peptide evaluation. These remain future work. |
| Compare reproducible scientific campaigns | Exact snapshots, per-call limits, provenance and saved replay | No demonstrated library-level comparison of strategies with matched opportunities, independent evaluation and campaign-level accounting. |

The implemented core is independent of loading optional engines, but is not yet
semantically provider-neutral. In particular, `InputRecord.issues` and
`results._row_issues` embody Macrel restrictions/columns. This qualifies the
stronger independence aspiration in the increment-1 prose. It is an extension
boundary to address before another assessor, not grounds to invalidate D35 or
replace its accepted behavior.

### 3.1 Finding register: defect, deliberate limit or missing capability?

| ID / classification | Evidence and consequence | Confidence / owner / disposition |
| --- | --- | --- |
| F1 — Reproduced diagnostic defect | `HydrAMPReceipt.issues` calls `math.isfinite` on a stored `10**400` integer and raises `OverflowError`, including after JSON roundtrip. An anomalous record cannot be inspected normally. | High for the two synthetic paths; no native model failure shown. PeptideMT #34, low priority for validated native output; fix with focused regressions separately. |
| F2 — Implemented semantic specialization | `inputs.py:55` and `results.py:70` impose the selected Macrel admission and result meanings. A new provider cannot inherit a generic contract merely from the type names. | High from source; deliberate initial scope. PeptideMT #33, review before a second assessor, preserve D35. |
| F3 — Declared identifier assumption | Two snapshots with the same caller-supplied ID/provenance but different scores can yield equal `Selection` objects, because those store references/ranking rather than full evidence or a content digest. | Reproduced with artificial data. Integration risk, not a proven contract violation. Retain the exact result artifact; investigate stronger evidence binding only at an approved persistence boundary. |
| F4 — Deliberate selection limit | Target/function metadata does not alter selection; duplicates can occupy several selected slots; missing heads are excluded. | Reproduced synthetic behavior, consistent with D35. Do not describe it as a faulty optimizer or silently change it. |
| F5 — Observed pool limitation | Both H4 pools lack any joint native AMP-positive/NonHemo row among their 15 eligible occurrences. No selection from those rows can create such a hit. | Exact finite observation plus logical inference; does not identify whether generation, predictive bias or limited sampling explains it. Scientific utility follow-up in #33/#32. |
| F6 — Unimplemented scientific operations | No current public redesign, adaptive-search or molecular-target operation exists in the inspected API. `n_target` is a count. | High for inspected source, not a claim about all future branches. Previously intended capability gaps; new commission required. |
| F7 — Unmeasured generalization | Current evidence does not quantify cross-resource data overlap, calibration on generated peptides, or broad predictive/biological utility. | Evidence gap, not proof of poor prediction. Measure for a chosen scientific endpoint; do not invent calibrated uncertainty or require it for every ranking. |

This register replaces a blanket verdict of correctness with claims whose
scope can be checked. F1 does not invalidate the valid native-output evidence;
F5 does not establish that HydrAMP is scientifically ineffective. F3 is especially
relevant when comparing campaigns: snapshot names are labels, not proof that two
analyses used the same values. The current saved-workflow example already
mitigates this by requiring exact file hashes and matching complete inputs.

### 3.2 Executed fixed-pool audit: what the selectors actually contribute

The instrument receives the two retained `seed_1001/1002-assessment.json` files
through `ResultSet.from_json`, after checking their original H4 SHA-256 hashes.
It calls only the existing selectors at `k=4` and performs ordinary arithmetic
on saved values. It does not rerun generation, Macrel, descriptors, molecular
operations or all previously accepted tests. Original files are untouched;
the [sanitized observations](evidence/peptidemt_scientific_audit_2026_11_04_observations.json)
contain counts, occurrence tokens and scores, not peptide sequences.

| Retained pool | Selected policy | Native AMP-positive / 4 | Native NonHemo / 4 | Both labels / 4 | Mean native AMP / Hemo score |
| --- | --- | ---: | ---: | ---: | --- |
| Seed 1001 | amp-first | 4 | 0 | 0 | 0.6782 / 0.7252 |
| Seed 1001 | hemolysis-first | 0 | 4 | 0 | 0.1386 / 0.0520 |
| Seed 1002 | amp-first | 4 | 0 | 0 | 0.6708 / 0.8812 |
| Seed 1002 | hemolysis-first | 0 | 4 | 0 | 0.1436 / 0.0173 |

Displayed means are rounded summaries only; exact stored scores and rankings
remain unchanged. These are uncalibrated native scores/labels, not expected
activity, percent lysis or a biological success threshold adopted by the audit.
No inferential statistics are justified from these two selected historical pools.

Each pool contains 16 distinct sequence strings, 15 eligible distinct strings
and one excluded leading-M proposal. Each shortlist contains four distinct
strings, and the two policies' shortlists have zero overlap within either pool.
Thus the selectors produce substantively different operational choices, but
neither achieves the illustrative joint-label condition. Among 15 eligible rows,
each pool has 12 distinct AMP scores; apparent score precision does not eliminate
ties. No causal explanation for those ties is inferred.

**Refuted interpretations:** these pools do not exhibit exact-string duplicate
collapse, so that cannot explain their zero joint-label yield. The finding does
not establish structural diversity or novelty, which were not measured. A new
selector cannot solve the absent-hit condition on these fixed pools. More samples
could change it, but no yield projection or new sampling budget follows. Neither
mean score nor a native label establishes actual antimicrobial or toxic behavior.

### 3.3 Controlled semantic walkthroughs

Five artificial scenarios make important limitations executable: opposed AMP/
hemolysis preferences choose different rows; adding an unassessed target/CPP
context leaves selection unchanged; duplicate occurrences can fill two slots;
different evidence with the same supplied ID can yield equal selection objects;
and a missing hemolysis head excludes its row. These are interpretation probes,
not five new scientific gates or a duplicate rerun of W1 acceptance.

A separate oversized numeric-field case reproduces F1 both in memory and after
serialization. That specific failure is a defect; the other observed behaviors
are consistent with the selected contract. The instrument exits successfully
because it explicitly expects and records the defect, not because all inputs
were successfully diagnosed. The Python source and outputs are hash-pinned in
the revision-2 receipt, with 1 GiB address-space and 15 CPU-second limits.

## 4. Prioritized improvements

Priority denotes expected contribution to the stated scientific purpose, not
permission to implement. No new biological threshold, selector or API is adopted.

### P1 — Make the scientific question and its evidence coverage inspectable

**Need:** a researcher must distinguish what was requested, what each operation
actually evaluated, and what remains unresolved. Current `context` preservation
is valuable but does not enforce endpoint-specific interpretation. `Outcome.eligible`
means eligible under the current result/selection contract, not biologically
acceptable. A qualification-reference string is explicitly a caller assertion,
not an automated certificate of applicability to every candidate.

**Proposed smallest deliverable:** a peptide-specific report for one existing
workflow, relating each declared requirement to the native result or explicit
coverage gap, selected policy and next useful evaluation. Reuse current snapshots;
do not first build a universal ontology, planner or confidence score. Generic
recording and scientific attribution remain with their ecosystem owners.

**Demonstrator:** an AMP/hemolysis request with a preserved unsupported proposal,
a predicted negative and a missing assessment. The report must distinguish
operational incompatibility, absent evidence, native negative prediction and
selection. A stored target name must remain visibly unassessed.

**Acceptance:** another researcher can explain every selection/exclusion from
the retained evidence, and no unmet requirement becomes satisfied merely because
the function returned successfully. This operationalizes accepted D09/D27–D32;
its concrete output contract needs review.

### P1 — Establish computational utility and fair comparison

**Need:** current evidence strongly tests faithful execution but does not show
that generation or a proposed search policy adds value at a useful cost.

**Proposed experiment design, not execution:** compare the two existing selectors
on the same fixed pool, then compare declared proposal methods using the same
assessment and selection. Include a supplied-pool baseline and one justified
simple procedural proposal control if approved. For redesigned candidates,
retain parent identity and compare against unchanged parents. Predeclare seeds,
budgets, allowed chemistry and unavailable internal costs before execution.

Report separately requested proposals, actual observable proposals, submitted
and completed evaluations, compatible rows, unique supported sequence views,
clusters under a declared metric, selected occurrences and outcomes of specified
operational checks. Count failures and reused results; a cache hit is not another
independent observation. Compare proposal/evaluation opportunities and resource
use, not only final shortlist size. Repeated seeds and correlated candidates do
not constitute independent biological replicates.

**Acceptance:** distinguish the contributions of generator, evaluator and selector;
show variability across the declared replicates and retain negative/inconclusive
outcomes. Report predictive yield as predictive yield, never experimental hit
rate. Do not set a numeric superiority margin after observing results.

The small H4 observation (zero joint native Macrel AMP-positive/NonHemo hits among
30 compatible generated proposals) is motivation to ask this question, not an
estimate of general failure probability or a reason to relax selection silently.

### P1 — Add purpose-specific selection only when a real decision needs it

**Need:** lexicographic preferences intentionally permit no tradeoff on the first
score. An arbitrarily small AMP advantage can outweigh a large hemolysis-score
difference. Likewise, preserving duplicate occurrences is essential provenance,
but selecting them need not maximize the value of a limited experimental batch.
Neither behavior is a bug in the current selectors.

For illustration only, invented score pairs A=(AMP 0.91, Hemo 0.90) and
B=(AMP 0.90, Hemo 0.10) select A under `amp-first`. This satisfies its contract;
it does not establish A as the preferable experimental candidate. The example
supplies no calibrated probabilities, new cutoff or assay conclusion.

**Proposed alternatives for review:** separate action prerequisites from ranking;
inspect optional contextual tradeoffs; select representatives under a justified
sequence/chemical diversity measure; inspect decision sensitivity when warranted.
Do not silently substitute Pareto selection for the current policies. A Pareto
front alone ensures neither feasibility, diversity nor biological relevance.

**Demonstrator/acceptance:** a fixed pool with close scores, duplicates, conflicting
objectives and missing evidence. Preserve the old exact rankings; any additional
policy must name its purpose, prerequisites, tie behavior, comparison set and
reasons. It must permit an empty or smaller-than-requested selection. New policies
require investigator approval before implementation.

### P1 — Implement and test genuine functional feedback after readiness review

**Need:** the major scientific step beyond the present pipeline is to use prior
evaluation to change a later permitted proposal, parent choice or allocation.
That fulfills the stated optimization objective much more directly than another
round of unrelated engine integration.

**Bounded candidate:** after a redesign operation is qualified, compare a declared
evaluation-guided parent policy with fixed/uninformed parent choice using the
same proposal operation and observable opportunity budget. Record parent-to-child
relations, allowed changes, all evaluations and actual later actions. A different
policy can also use repeated de novo calls if its exposed controls make the
scientific intervention meaningful; seed changes alone do not prove guidance.

**Acceptance:** an intervention changes actual subsequent inputs/actions, the
decision trail replays, and the matched control measures utility/diversity/cost.
Failure to outperform the control is a scientific outcome, not permission to
change the benchmark. Higher reward alone does not establish better biology.

The risk of optimizing model errors under distribution shift is established in
general model-based optimization ([COMs](https://proceedings.mlr.press/v139/trabucco21a.html));
[CbAS](https://proceedings.mlr.press/v97/brookes19a.html) explicitly formulates
design using predictive distributions. These are motivation and methodological
precedents, not peptide-specific validation or recommendations to adopt either
algorithm without testing its assumptions. Preserve a separate assessment role
where feasible; repeatedly tuning against it makes it part of search.

### P1 strategic — Deliver one target/function case without waiting for every family

**Need:** joint target/function design is central to the investigators' purpose.
An indefinitely expanding AMP integration programme could miss that purpose even
if every adapter is technically excellent. Completing every original HydrAMP
training feature is not a necessary prerequisite for PeptideMT's target milestone.

**Proposed bounded scope:** select one target, one chemically supported peptide
modality and one functional endpoint; qualify a permitted target-capable route.
Name an antitarget or missing selectivity evidence when relevant. Compare the
target-first/family-assessed baseline with an alternative only when actual
operations support a meaningful comparison. No target model is selected here.

**Acceptance:** document whether the target affected proposal generation,
evaluation, selection or none; separately report functional assessment,
recognition evidence and unsupported requirements. Docking, complex confidence,
sequence compatibility and affinity must not be renamed into one quantity.
Target conditioning alone is not recognition validation.

This can be planned alongside feedback, as the accepted trajectory already
envisages. Its value depends on availability, terms and supported chemistry;
no promise of a live case or target-specific biological success follows now.

### P2 enabling — Grow beyond one evaluator with explicit scientific bindings

**Need:** optional imports and arbitrary dictionaries do not establish model
substitutability. CPP uptake, endosomal escape, cytosolic access and cargo delivery
are different endpoints. AMP/CPP/ACP can overlap and should not be forced into
exclusive classes. Absence of annotation is not a measured negative.

**Proposed deliverable:** when a second real assessor is selected, review the
smallest operation-specific binding for subject/view, endpoint/context, units or
score semantics, direction, applicability, provenance and unavailable results.
Keep native results and the current Macrel adapter intact. Demonstrate two
heterogeneous resources before generalizing further; do not invent a universal
registry merely to rename current classes.

**Acceptance:** unsupported input in one route remains available to a qualified
other route; the current Macrel results/rankings replay unchanged; incompatible
endpoints cannot be averaged or multiplied into fictitious joint probabilities.
Owner-specific defects go to the provider's own issue, subject to external
publication permission where required.

### P2 enabling — Make applicability, novelty and chemical views usable evidence

**Need:** a valid canonical sequence is not necessarily within either head's
empirical domain. Score saturation is not certainty. Adding a predictor does not
automatically provide independent validation. Similarity to a training set is
only measurable when the relevant data/version are actually available.

**Proposed work:** inventory each resource's training/evaluation sources and
negative-label construction; report known overlap and unknown dependence;
stratify future benchmarks by justified length/composition/sequence clusters;
assess external predictive performance and calibration if relevant labeled data
permit. Novelty needs a declared reference corpus and metric. Do not equate
sequence novelty with a new mechanism or infer confidence intervals from model
disagreement. Calibration is desirable where probability claims matter, not a
universal prerequisite for exploratory ranking.

For chemistry, preserve the existing conservative route. Select one actual
future transformation/representation only when the task needs it; retain parent,
realized species and evaluated view. A C-terminal amide, D residue or cyclization
cannot inherit a parent sequence's scores by default. MolSysMT owns topology,
molecular representation, reading, construction and mutation; TopoMT owns
topography. Missing shared capabilities need owner proposals, not local copies.

**Acceptance:** model applicability and chemical attribution remain explicit,
including unknowns. Computational completion remains possible without new assay
data. Such data, when available, would strengthen a separate biological claim.

### P2 enabling — Improve scientific usability and status navigation

Current user routes expose many necessary low-level identities/limits, but do
not yet supply a compact scientific campaign comparison or a complete standalone
workflow portable to another authorized installation. Preserve explicit resource
control while reducing repeated manual setup through reviewed profiles when
supported. Check user needs before adding a CLI, web UI or more infrastructure.

The design guide and roadmap contain historical pending statements next to later
acceptances. The first audit also found stale provider docstrings. A current
capability/evidence table should lead navigation, with historical reasoning
clearly dated. Audit notices must not silently turn pending capabilities into
accepted ones. The A1 pause record explicitly owns the unfinished instruction
synchronization; it must be resolved before implementation resumes.

**Acceptance:** a researcher can identify the supported route, evidence limits,
input requirements, selected artifacts and reason for every outcome without
reconstructing the entire development chronology. A saved replay remains clearly
different from new inference. This is a product demonstration, not a benchmark
against better biological outcomes.

## 5. Recommended sequence and stop conditions

Revision 1 assigned P1 to too many opportunities to establish a useful working
order. The following ordering is the revised recommendation. The eight areas
above remain a capability inventory, not eight simultaneous priorities.

| Next decision | Why now | Evidence to advance / reason to reconsider |
| --- | --- | --- |
| First: review a concrete evidence-coverage report and utility comparison specification for the present AMP route | Directly addresses F5 without adding a model or guessing a new architecture | Traceable denominators, unmet endpoints and declared comparisons. The saved-pool audit is descriptive groundwork, not a prospective efficacy experiment. |
| In bounded maintenance: fix F1 and clarify evidence binding/current status | Makes current results safer to inspect and reuse; independent of scientific expansion | Malformed payloads remain inspectable, exact valid behavior preserved, no new biological thresholds. F3 needs an explicit contract if persistence changes. |
| Next capability: qualify a limited redesign operation when explicitly unpaused, then consider one feedback experiment | Supplies a controllable proposal operation and tests actual optimization | Separate provider/consumer qualification, causal later-action change and an equal-opportunity no-feedback control. No reward gain alone establishes utility. |
| Parallel strategic review: choose one feasible target/function case | Protects the original scientific objective from indefinite AMP/provider-only work | Actual endpoint, chemistry, permissions and capability feasibility; stop if target metadata is the only available target contribution. Full HydrAMP training is not a prerequisite. |
| Later as needed: broaden families, chemistry and selection | Demand-led breadth avoids unsupported abstractions and duplicated responsibilities | A concrete task that existing operations cannot address, with owner-supported representations and independent new evidence. |

Owner map: PeptideMT owns peptide-specific design, interpretation, selection and
search policy. Providers own model methods and their bugs. MolSysMT and specialist
suite components own molecular operations. Review Recorda, Praxis, Ackredit and
other applicable supported boundaries before building generic record/workflow/
attribution machinery. No new cross-component implementation is proposed as an
already available capability.

### 5.1 Prospective utility study: decisions required before execution

This is a study specification checklist, not an approved campaign or a promised
success threshold. It makes the recommendation falsifiable without inventing a
sample size, biological ground truth or universal scalar fitness.

| Design item | Proposed requirement for the first comparison |
| --- | --- |
| Primary question | State whether the study tests proposal yield, selection decisions or feedback. Do not change the question after seeing unfavorable scores. |
| Arms | For selection, use one identical fixed pool. For proposal value, compare the reviewed generator with a fixed supplied pool and a justified simple proposal control. For feedback, compare the same proposal operation with an uninformed/fixed policy. No unimplemented arm is labelled executed. |
| Frozen choices | Fix assets, evaluated views, seeds, task restrictions, native settings, policies, budget, operational success conditions and analysis before execution. Native joint labels may be an exploratory metric, not a new scientific acceptance rule. |
| Primary denominator | Report operationally qualifying **occurrences / all observable proposed occurrences**, alongside **qualifying / assessed** and **assessed / proposed**. Keep unobservable internal attempts explicit; do not silently use the smaller favorable denominator. |
| Additional views | Report exact-string uniqueness separately from molecular identity, qualified diversity/novelty metrics when available, exclusions by cause and cost by actual observed work. An input incompatible with one route is not a biological negative. |
| Replication | Use declared independent runs/starting pools where feasible. Analyze run-level variation and shared ancestry rather than treating every correlated candidate as an independent replicate. Select sample size/precision after a cost/data assessment, not from these two historical seeds alone. |
| Comparator fairness | Match declared proposal/evaluation opportunities and disclose startup/reuse/hidden-work differences. Equal final candidate counts are insufficient. A chemically invalid control would not be an informative baseline. |
| Independent assessment | Where available, separate search rewards from assessment and examine data overlap. Without an independent endpoint, restrict the claim to performance under the named predictive criterion. More agreeing predictors alone do not supply independence. |
| Stopping | Fix resource and futility/no-progress rules prospectively; retain all failed/empty runs. No unrecorded refill, relaxed constraint or best-seed-only report. |
| Decision after results | Advance if the predeclared useful effect is supported at its required precision/cost; otherwise narrow, defer or change the scientific hypothesis explicitly. Feasible computation, favorable native scores and biological efficacy remain different conclusions. |

The next bounded artifact recommended here is this specification completed for
one actual task, plus a scientist-readable coverage report on existing evidence.
It does not require a universal campaign class, extra model integration or
immediate training. A new broad report without a chosen question would add less
value than resolving the specific comparison and observability limits.

## 6. Is this audit complete? How should it improve?

**The original audit was not complete for PeptideMT. Revision 2 is more
decision-useful, but still not an exhaustive validation.** It adds objective
coverage, product versus provider separation, executed semantic counterexamples,
fixed-pool quantitative observations and a prioritized study specification.
The distinction between confirmed defect, intentional scope, integration risk
and missing empirical evidence is now explicit.

Still missing:

- A real user completing a representative design task unaided; usability has
  been inspected, not measured.
- An independent full code/test review, current coverage analysis, security and
  scaling measurements. Test counts do not measure scientific correctness.
- A systematic literature/tool landscape and permitted dataset inventory for
  a selected target or new functional endpoint.
- Measured cross-model training overlap, generalization/calibration and a
  prospective comparative utility experiment.
- Any claim that the proposed priorities are optimal for investigators' actual
  experimental resources. Their cost/value ordering is reasoned advice, not
  measured return on effort.

A better next audit should use one chosen scientific task as an acceptance
walkthrough: specify what success means computationally, run only its approved
operations, inspect actual outputs and ask which decision the library improved.
Track progress by new scientific operations and interpretable evidence, not
documentation volume, integration count or raw number of generated peptides.

Implementation of these improvements, new models/chemistry, training, target
design, feedback and scientific execution require their own concrete disposition.
D35/M1–M8, accepted resources, selector semantics and the analogue pause remain
unchanged. HydrAMP modernization and PeptideMT evolution can proceed as related
projects with separate completion criteria; neither must absorb the other.
