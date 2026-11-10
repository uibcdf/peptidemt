# MDM2 T0 implementation checkpoint

Historical checkpoint: superseded as current status by the
[completed T0 qualification](mdm2_t0_qualification.md), 2026-11-06. The sections
below retain the earlier checkpoint and its then-applicable limits/failures.

Historical status: **implemented case coordinator and artificial interpretation checks;
exact installed profile and real geometry still pending**, 2026-11-05.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Authority: D51 and the [authorization](evidence/mdm2_t0_authorization.json),
which binds the exact reviewed [work order](mdm2_t0_work_order.md).

## Delivered behavior

[The development coordinator](../devtools/mdm2_t0.py) receives this one bounded
public source package, checks the exact qualified profile before dispatch,
delegates molecular interpretation and geometry to MolSysMT, compares the three
views with the fixed T0 criteria and inspects saved results without importing
molecular providers or recalculating geometry. It introduces no public PeptideMT
API, selector, reusable molecular parser or molecular geometry implementation.

The geometry path retains raw source/revision metadata, source/native atom maps,
author/label/native chain identities, occupancy/alternate observations, conversion
report and inferred-connectivity evidence. It keeps source model identifiers
separate from native structure indices/IDs. Numerical arrays have explicit units;
nm extraction is explicit under a non-default application unit policy. The
worker applies the approved bounds and forbids network/unplanned children.
Source/profile/observation failures stop before geometry; actual warnings and
failure details are retained. These are implemented obligations, not delivered
runtime evidence for an unexecuted path.

## Actual source receiving

The official [RCSB history](https://www.rcsb.org/versions/1YCR) supplies the
versioned reference link. The requested revision-1.5 archive was received once:

- compressed mmCIF: 32,669 bytes, SHA-256
  `f764bf016f4f294afb905ee447a64362c7da9a700846cfe2b51db6cad739fbd2`;
- expanded mmCIF: 121,649 bytes, SHA-256
  `03f62994ea1ff55d98c0d9d835b706319e523367fce56d9deb51b850c83e47a8`.

The acquisition manifest also retains the entry/revision/usage pages and one
official validation PDF, with actual URLs, timestamps, sizes, headers and hashes.
The report is independently dated; its association with these exact coordinate
bytes is not established. Source bytes are received, but internal molecular
identity/revision and coordinate coverage have **not** yet been checked through
the qualified owner reader. No local parser replaces that pending operation.

## Executed checks

[The focused tests](../devtools/tests/test_mdm2_t0.py) pass **11/11** with native
pytest exit 0 and published Pytest Receptor 1.2.2. They use artificial returned
arrays to test the fixed interpretation, erased-displacement false positives,
rigid drift, spurious contacts, boundary-band handling, malformed/missing evidence,
saved-file/unit integrity and rejection of an unqualified profile. They do not
exercise molecular parsing, alignment or real contacts/RMSDs. No molecular or
learned provider is imported during these tests. Peak sampled aggregate RSS is
91,504,640 bytes; the 1 GiB stop and 8 GiB host reserve remain applicable.

`ruff check .` and `ruff format --check .` pass over the current repository
(200 formatted files). These static checks and artificial assertions establish
neither scientific qualification nor the installed MolSysMT profile.

## Installed-profile gate and retained failures

The source-only MolSysMT checkout at
`ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6` is isolated under this task. The
original shared editable checkout remains at
`71fbe4f46d3c70e4e973c8025f01752a8c9b1084`; no shared installation is switched.
The isolated native build uses the supplied environment tools offline and one
Cargo job. Its separately declared engineering bounds are 1 GiB aggregate RSS,
8 GiB host reserve, 8 GiB address space, 300 s wall/240 s CPU and 2 GiB build
output; these do not replace the narrower numerical-worker bounds.

The first two installation attempts were terminated by `host_resource_guard`
when available RAM crossed below the reserve. Their sampled aggregate peaks
were 199,979,008 and 196,415,488 bytes. Neither is a completed installation or a
MolSysMT defect reproduction. Preserve both failures and the partial private
build cache; do not label the shared older reader as this exact source profile.
An import/native-origin, dependency and unit-policy probe is prepared for after
a completed installation. It has not passed merely because a venv exists.

The [checkpoint receipt](evidence/mdm2_t0_implementation.json) records the actual
source files, engineering attempts, artificial tests, static checks and final
profile/geometry status. Review that record for the later bounded headroom
observation and any additional attempt; do not infer success from this plan.

## Continuation and scope

Once adequate host headroom is available, complete the same isolated profile,
run its actual receiving probe, then dispatch the three-view case serially and
inspect its retained results. Existing source downloads and passed interpretation
tests need not be repeated without a relevant change. No fresh per-invocation
permission is required under D49/D51. Changed scientific criteria or a materially
larger allocation retains its separate boundary.

T0 remains incomplete until source/profile admission and all actual geometry
gates finish honestly. Even a passing T0 establishes observed-coordinate identity
and numerical handling only. T1 recognition, affinity, biological utility,
docking, generation, models/GPU, public APIs, Git consolidation and publication
remain outside this work.
