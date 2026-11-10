# MDM2 T1a qualification: reported-affinity reference

Status: **completed within the approved D53 data-only scope**, 2026-11-09.
Local source and private developer-artifact delivery; no commit or publication.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Authority: [approved work order](mdm2_t1a_work_order.md) and
[approval receipt](evidence/mdm2_t1a_authorization.json). The original
[proposal](mdm2_t1a_proposal.md) retains its exact reviewed bytes and historical
status. The [execution receipt](evidence/mdm2_t1a_qualification.json) identifies
the actual sources, code, profiles, outputs, controls and failures.
The [owner-issue outcome](https://github.com/uibcdf/peptidemt/issues/33#issuecomment-6759965592)
is published and read back exactly; [closeout checks](evidence/mdm2_t1a_closeout.json)
retain the documentation checks and publication receipt. The parent issue remains open.

## Delivered behavior and source reconciliation

The private [case receiver](../devtools/mdm2_t1a.py) receives the previously
acquired main HTML of [Li et al. (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2856455/),
DOI `10.1016/j.jmb.2010.03.005`, Tables 1 and 3 and their source context.
The article bytes remain SHA-256
`99f361fdab13c2971362fbe5e96b255e8a32dd5f8d605154bcd98918268f1264`;
the original acquisition receipt and its original date are preserved.
No new acquisition, supplement access or molecular interpretation was needed.

| Retained population | Actual result | Meaning |
| --- | ---: | --- |
| Displayed peptide rows | 36 | 18 in each table; source order retained |
| Peptide–target occurrences | 72 | Both MDM2 and MDMX columns for every displayed row |
| Explicit repeated-display occurrences | 2 | PMI WT/A4 self-substitution display, one for each target |
| Source-scoped reported peptide identities | 35 | Source bookkeeping after that explicit alias; not certified unique molecules |
| Reported peptide–target evidence records | 70 | Original occurrences retained through alias links |
| Quantified evidence records | 66 | Kd and its stated SD, each in molar concentration units |
| Unquantified evidence records | 4 | Table 3 HTML rows 6 and 10, for both targets |

Table/row/column locators, all literal cells, source precision, unavailable
tokens and curation reasons survive receiving and replay. The repeated PMI
display is linked to the original reported evidence, rather than promoted to
an independent experiment. Other molecular equivalence is not inferred.
The Table 3 caption's stated p53/analogue count conflicts with its 18 displayed
rows; all displayed rows are retained and the discrepancy is explicit.

The source's common exponent applies to both printed Kd and SD. Exact decimal
strings remain alongside the literal tokens; numeric records use explicit
`mole/liter`. PyUnitWizard's public `MeasurementRecord` owns serialization and
quantity/uncertainty validation. PeptideMT adds the case's source correspondence
and scientific eligibility checks, not a replacement physical-unit codec.
The source lower bound of three independent measurements is retained separately
from an unknown exact replicate count. SD remains SD, with no confidence level,
standard error, thermodynamic conversion, pKd or activity threshold invented.
Weak binding reported as not determined retains no numeric value or exact
censoring limit.

## Actual qualification and profiles

The [artificial controls](../devtools/tests/test_mdm2_t1a.py) pass **22 tests**
under Pytest Receptor **1.2.2 from its retained published wheel**, with native
exit status 0 and JUnit evidence. They cover duplicate inflation, target swaps,
lost occurrences, unknown-chemistry promotion, incompatible units, altered
quantity seals, false replicate counts, unavailable-to-number coercion, changed
source pins, lost acquisition provenance and malformed saved JSON. Artificial
fixtures are presentation tokens, not experimental peptide evidence.

After those controls passed, the actual source was received **once**, using the
existing isolated fixture, without reinstalling or rebuilding it. Its current
dependency check and an actual synthetic measurement-codec probe pass. The
receiving profile is Python 3.14.7, PyUnitWizard
`0.29.0+4.g9d74f0e` at
[`9d74f0e1e911d78c1906948e74ce8da93935557d`](https://github.com/uibcdf/pyunitwizard/tree/9d74f0e1e911d78c1906948e74ce8da93935557d),
Pint 0.26.2 and NumPy 2.4.6. The profile receipt retains the other support
versions and hashes of the actually imported provider modules. This qualifies
this development codec route, not a public released dependency combination.

A separate bounded cross-check matches **all 72 measurement tokens** to explicit
table expectations, checks all four unquantified locators and both aliases,
and checks five independently stated decimal Kd/SD pairs spanning the tables
and exponent range. This verifies transcription and interpretation of the same
source; it is not independent experimental corroboration.

An unchanged copy of the saved artifact then passes inspection in a **fresh
process**, starting from a directory containing only that artifact. It retains
the original producer identity and uses the routine
`molsyssuite@uibcdf_3.14` profile, with the same PyUnitWizard revision and Pint
0.25.3. Original article-file access is blocked in that reader; it rechecks the
embedded source and acquisition record instead. Neither receiving nor replay
imports a molecular or learned provider. Explicit unit restoration and caller
unit-policy preservation also pass. This is observed saved-record compatibility
between those two concrete profiles, not a general compatibility promise.

The saved reference SHA-256 is
`b9af350ef8a39febcb807c18c7d56d8a11391c2c6284ab689ac9d3293007cea6`
(582,445 bytes). Its full article/data contents remain private in the task
directory identified by the receipt. They are not added to maintained/public
documentation. The executed case source is SHA-256
`df7ed5677f52abaab698289d4137467bd0068c9029a714a875acc5c1a9724307`.

## Failures, resource use and limits

The shared environment's `pip check` fails on the already reported Amber-extra
requirements tracked in [MolSysSuite #82](https://github.com/uibcdf/molsyssuite/issues/82):
missing `pdb2pqr` and NumPy/Biopython version constraints. Its successful
measurement probe does not cancel that failure or qualify the entire shared
environment. The isolated receiving fixture passes `pip check`. No unrelated
component or shared package was modified to repair the ambient check.

One saved-reader shell launch used an incorrect interpreter path and failed
before its controller or worker started. Its failure record is retained; using
the verified interpreter path succeeds with the same artifact and code. This
was an orchestration error, not a source or quantity-provider defect. No source
receiving or model call was repeated to correct it.

Jobs ran sequentially under the approved CPU0/1, one numerical thread,
512 MiB aggregate sampled RSS and 4 GiB available-host-RAM reserve profile,
with the approved time/output/address-space limits. The largest sampled
controller/worker RSS was **111.95 MiB**, in the tests. Receiving used
77.97 MiB and 0.87 s; saved inspection used 99.04 MiB and 0.82 s. No guard was
breached. These are sampled measurements, not continuous physical-memory
maxima. No GPU, molecular preparation or neural evaluation ran. Accepted T0
geometry and HydrAMP evidence were preserved and not repeated.

## Scientific disposition and next decision

**Suitable now:** an auditable reference of this article's reported SPR-competition
Kd/SD evidence, with distinct target/construct contexts and honest unknowns.
It supports a concrete subsequent evaluator-domain proposal and source review.

**Not established:** exact terminal chemistry, stereochemistry, modifications,
construct-to-coordinate correspondence, chemical uniqueness, training-data
independence, prospective blinding, peptide-affinity prediction or useful
selection. The reported constructs remain MDM2(25–109) and MDMX(24–108); MDMX
has no adopted off-target or co-target objective. Room temperature remains a
reported condition, not an invented numeric temperature. The supplement was
not received. Public readability is not a dataset-redistribution license.

Consequently, this panel can inform retrospective method development after its
domain is agreed; it cannot yet serve as an independent chemically qualified
prediction benchmark. Results were exposed before method choice. Any later
utility claim needs an explicit exposure/leakage policy and a justified separate
evaluation reference or an honestly bounded retrospective design.

The next scientific contract should fix the molecular/assay domain, resolve
chemical source gaps through owner-supported MolSysMT operations, select a
provider for the actual observable, and prespecify baselines and refutation
criteria. [MolSysMT #685](https://github.com/uibcdf/molsysmt/issues/685) records
the future reusable chemical-profile need; it did not block this data-only work.
The [method review](target_directed_method_review.md) still separates peptide
pose evidence from affinity and selection utility. No evaluator or candidate
generation is adopted by T1a's technical completion. The original D52
target-directed design/selection objective and parent #33 remain incomplete.
