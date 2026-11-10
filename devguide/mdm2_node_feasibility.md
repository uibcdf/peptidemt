# MDM2 pilot preparation: node and five-node infrastructure feasibility

**Investigator correction / migration checkpoint, 2026-11-10:** the intended
development machine is a **different machine**, to which work is moving now.
All measured CPU/RAM/disk/PCI/driver values below describe the **source machine
only**. They are not destination-node specifications or admission evidence.
The planned five-node/GPU deployment remains an investigator-reported plan;
neither the destination nor the other nodes has been inspected. Reinventory the
actual destination before choosing execution profiles. The read-only MolSysMT
result remains valid evidence for its original source machine/composition.
Use the [migration checkpoint](migration_checkpoint_2026_11_10.md) to resume.
The original measurement receipt is retained unchanged; this correction does
not relabel old observations as measurements of the destination.

Status: **preparation and read-only feasibility review delivered**, 2026-11-10.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
This extends the [pose-pilot proposal](mdm2_comparative_pilot_proposal.md),
following the investigator's instruction to prepare its molecular/provider
profile and assess work before the new GPUs arrive. The proposed scientific
pilot, chemistry and model runs remain separate from this preparation.

## Recommendation

**Begin with CPU molecular preparation and owner-led HADDOCK3 receiving on the
present infrastructure. Do not wait for all five new GPUs to make progress.**
The present node has adequate measured headroom for the read-only MolSysMT
inspection executed below. HADDOCK3 is a plausible CPU candidate, not an installed
or memory-qualified docking route. Its provider, chemistry and actual bounded
runtime must still be received before docking.

Prioritize **one RTX 5070 Ti for the first small Boltz-2 pose qualification**
after its arrival, driver/provider admission and an explicit GPU execution
commission. A 16 GB card is a better first candidate than a 12 GB card; neither
has been measured here. Do not attempt Boltz-2 loading under the current 2 GiB
host-RSS ceiling merely because its CLI accepts CPU. BindCraft/BC2/BoltzGen remain
later generation alternatives, with separate scientific and resource contracts.

## Inspected source machine, not the destination or all five nodes

Read-only observations at 2026-11-10 15:49 UTC, with mount/build clarification
later in the same review:

| Resource | Observed state | Consequence |
| --- | --- | --- |
| Processor | Xeon E5-2630 v4, 10 physical cores/20 logical CPUs, AVX2 | Suitable architecture for CPU preparation and a serial classical-route assessment; no measured docking throughput |
| Host RAM | 30.68 GiB total; 22.93 GiB available at inspection | Headroom exists now; availability must be rechecked for each job |
| Load | Approximately 0.20/0.15/0.18 | Light at inspection, not a reservation of the shared node |
| Workspace | Rotational 3 TB-class disk, about 2.27 TiB free | Storage capacity is not the immediate obstacle; no I/O benchmark was run |
| Root storage | 128 GB-class NVMe, about 74.65 GiB free | A possible future explicitly sized cache location; nothing was moved |
| `/tmp` | RAM-backed tmpfs | Keep large weights and environments in disk-backed task storage |
| PCI graphics | GTX 1080 and Quadro M2000 | Hardware detection only; usable CUDA memory was not measured |
| Driver query | `nvidia-smi` exit 9, cannot communicate with NVIDIA driver | No working CUDA execution route is verified on this node |

HADDOCK3/CNS and Boltz are absent from the inspected shared profile and PATH.
Installed Torch metadata says 2.10.0; its `version.py` declares CUDA 13.0.
This was read without importing Torch or launching a GPU kernel. It establishes
neither driver compatibility nor a working model installation.

The standing preparation envelope remains one serial job, CPU0/1 affinity,
one numerical thread, nice 10 for the numerical child, a sampled **2 GiB aggregate
supervisor/worker RSS stop**, at least **4 GiB available host RAM**, bounded
wall/CPU/output and 8 GiB virtual address space. Physical free RAM does not
silently increase that allocation. No GPU computation or driver change occurred.
These limits do not replace the separate historical HydrAMP/D50 envelopes.

## Actual molecular preparation evidence

The new question was chemical-field/template coverage of the already admitted
1YCR reference, not repetition of accepted T0 geometry. The existing qualified
MolSysMT composition at `ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6` was reused,
with its existing Python prefix and native extension. Selected source/native
pins and import origin were checked; full dependency qualification was not rerun.
The original source SHA-256 remains
`03f62994ea1ff55d98c0d9d835b706319e523367fce56d9deb51b850c83e47a8`.

One public conversion and one `msm.build.get_residue_chemical_coverage` request
returned the owner's embedded chemical-readiness report:

- 818 atoms and 98 assessed groups; no missing heavy-atom names in the examined
  standard residue templates. This is template coverage, not validation of
  terminal chemistry, side-chain stereochemistry or the experimental construct.
- Zero explicit H atoms; hydrogen-template interpretation remains unassessed
  for all 98 groups. Formal charge and atom stereochemistry fields are missing;
  bond orders/aromaticity coverage is partial and connectivity is declared partial.
- Environmental protonation, terminal context, inter-group chemistry, valence,
  force-field coverage and docking readiness remain unassessed.

The corrected receiving job completed in **2.72 s**, with **201.04 MiB sampled
aggregate RSS**. This measures this read-only request only, not HADDOCK3, Boltz-2
or a general preparation budget. The first attempt completed the owner request
but our local JSON writer failed on NumPy arrays: exit 1, 14.96 s, 200.16 MiB.
The original code, failure and declaration are retained. One diagnosed retry
added array/scalar value encoding, without changing molecular settings. Its
separate retry-reason record governs classification; the generic supervisor's
per-invocation `retry: false` is not a claim that no earlier attempt occurred.
Neither attempt assigns states, adds atoms, changes coordinates or runs a model.

See the [input-profile preparation](mdm2_input_profile_preparation.md) for what
this allows us to specify and what still requires scientific/owner resolution.

## Feasibility by approach

| Approach | Present node | New 12/16 GB GPUs | Remaining evidence |
| --- | --- | --- | --- |
| MolSysMT input inspection, correspondence and retained-result checks | Demonstrated for the one read-only coverage request; existing T0 geometry is reused | Not needed for this preparation | Freeze the actual chemical and transport recipe |
| HADDOCK3 classical flexible docking | CPU route is a sensible first qualification candidate; engine/provider not installed/received | GPU arrival is unnecessary for the proposed CNS route | CNS terms/binary, exact owner profile, chemistry, sampling, observed RAM/time |
| Boltz-2 fixed-pair complex prediction | CPU option exists; no qualified fit in 2 GiB and no practical runtime measurement | First assess one 5070 Ti; small 98-residue case is promising, not a fit guarantee | Exact bundle, owner boundary, inputs/MSA/template, compatible kernels, host RSS and VRAM measurements |
| Original BindCraft | Not a CPU route recommended by its authors | Small cases may merit later receiving, but 12/16 GB are below its 32 GB recommendation for larger complexes | JAX/AF/PyRosetta closure, numerical compatibility and separately commissioned generation |
| BindCraft2 | Inspected installation explicitly refuses CPU installation | Small padded cases may be possible; never enable its automatic worker packing on this shared host | Exact case/model path and GPU/host memory admission; generation remains uncommissioned |
| BoltzGen, Chai-1 and other reviewed neural routes | Source/configuration review can proceed without models | Case- and pipeline-dependent; five cards do not guarantee any single large model fits | Their separate runtime/terms/precision/VRAM profiles; no adoption follows from this table |

[HADDOCK3 execution settings](https://www.bonvinlab.org/haddock3-user-manual/global_parameters.html)
allow local CPU execution. Explicitly prescribe `ncores = 1`; the default is
four and `max_cpus = false` alone would not protect this shared host. Module
overrides must obey the same limit. The inspected source
[`29a37103…`](https://github.com/haddocking/haddock3/blob/29a37103bb4648f3e4c3245cefa8c7ffadc1c431/pyproject.toml)
declares Python >=3.10,<3.15. That includes 3.14 syntactically, without proving
a complete install or native CNS receiving. Its
[CNS disclaimer](https://github.com/haddocking/haddock3/blob/29a37103bb4648f3e4c3245cefa8c7ffadc1c431/DISCLAIMER.md)
must remain separate from HADDOCK3's Apache-2.0 code license. No installation,
CNS acquisition or license acceptance was performed.

Boltz's pinned
[CLI source](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/src/boltz/main.py)
supports CPU and warns it will be slow. Multi-device execution uses DDP and
reduces device count when there are fewer inputs; it does not expose transparent
pooling of VRAM for this single complex. Boltz-2 uses `bf16-mixed`, and its data
loader defaults to two workers. Any future serial profile must make these
choices explicit. The default acquisition path also retrieves affinity weights
even for a structure-only question: acquisition scope must be reviewed before
running the CLI. No checkpoints were downloaded.

[BindCraft's recommendation](https://github.com/martinpacesa/BindCraft/blob/7713aa0d0d351e4117a8befeb8541f3a8ebd3368/README.md)
is 32 GB for larger complexes, not a universal minimum. The inspected
[BC2 installation contract](https://github.com/PacesaLab/BindCraft2/blob/8c1a858fdc1bfc94c60846ff11a0d01c9aa44136/docs/source/installation.md)
estimates per-worker memory using padded residue count, reserves 4 GB of GPU
headroom and budgets 4 GB host RAM per worker. Those are upstream planner
estimates, not measurements of our case. Its default may pack several workers
per visible GPU; that is incompatible with our current serial intent.
[Chai-1](https://github.com/chaidiscovery/chai-lab/blob/c691da74d6f348b19bc9f931abe95d66d0b88e78/README.md)
recommends larger accelerator memory while allowing smaller complexes on other
cards. [BoltzGen](https://github.com/HannesStark/boltzgen/blob/6472b44e8072187e6eaa51271ae6838245206013/README.md)
has a multi-stage runtime/acquisition closure. Download size is not resident RAM
or VRAM, and neither is a complete scientific campaign budget.

## Five-node plan and mixed GPU generations

The investigator reports **five similar nodes total**, planned PSU/fan upgrades,
two RTX 5070 Ti and three RTX 5070 distributed within that infrastructure, plus
existing 2080-series cards (Ti status uncertain) and GTX 1080s. Only this node
was inspected. Counts, exact board variants, actual RAM/driver/storage on the
other nodes and final card placement remain unmeasured.

A practical **proposed allocation is one new card per node**, starting with one
job on one 5070 Ti. Additional independent seeds/cases may later be dispatched
to other nodes only within their own admitted resources and scientific budgets.
Do not introduce distributed model training or a PeptideMT-local cluster manager
to conduct this small pilot. A five-node installation increases potential
throughput; it does not make a single job's RAM/VRAM limits disappear.

| Card family | Manufacturer memory / architecture | Planning interpretation |
| --- | --- | --- |
| RTX 5070 Ti, two planned | 16 GB each; Blackwell, CC 12.0 | Preferred first small cofolding qualification candidate |
| RTX 5070, three planned | 12 GB each; Blackwell, CC 12.0 | Independent workloads that are demonstrated to fit; no guaranteed support for every generator |
| RTX 2080 Ti / RTX 2080, exact inventory pending | 11 GB / 8 GB; Turing, CC 7.5 | Qualify a compatible older-card profile; do not assume Ti memory or native BF16 behavior |
| GTX 1080 and observed Quadro M2000 | Legacy CC 6.1 / 5.2 | Potential legacy-compatible work, not the default current Boltz-2/Blackwell environment |

Sources: [NVIDIA 5070 family](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/),
[older GeForce memory comparison](https://www.nvidia.com/en-eu/geforce/graphics-cards/compare/),
[current compute capabilities](https://developer.nvidia.com/cuda/gpus) and
[legacy compute capabilities](https://developer.nvidia.com/cuda/gpus/legacy).
The new cards provide 68 GB in aggregate across five devices, **not a single
68 GB model device**; NVIDIA lists no NVLink on either new model.

Keep separate qualified environments by actual architecture/runtime needs.
Blackwell needs a compatible driver, CUDA-enabled framework and model kernels;
CC 12.0 is an architecture identifier, not a request to install CUDA toolkit 12.0.
[PyTorch 2.7 introduced Blackwell/CUDA 12.8 builds](https://pytorch.org/blog/pytorch-2-7/);
this is historical compatibility evidence, not an instruction to downgrade the
shared environment or proof that every model dependency supports the cards.
[CUDA 13 removed Maxwell/Pascal offline compilation and library support](https://docs.nvidia.com/cuda/archive/13.0.0/cuda-toolkit-release-notes/index.html).
The shared Torch build declaring CUDA 13.0 must therefore not be presumed to
serve the GTX 1080/M2000. Per-environment CUDA selection also cannot repair an
incompatible node-wide driver branch. Mixing old and new cards in one node
needs actual driver/framework compatibility receiving.

The pinned Boltz-2 BF16 setting is an additional older-card gate.
[Lightning's precision documentation](https://lightning.ai/docs/pytorch/stable/reference/common/precision_intermediate)
does not make its BF16 benefits universal across GPU generations. Do not quietly
change to FP16/FP32 or disable kernels and call it the same qualified numerical
profile. Neither the Turing cards nor the Pascal card were tested here.

The observed board is a Gigabyte X99-Ultra Gaming-CF; the
[manufacturer's corresponding specification](https://www.gigabyte.com/us/Motherboard/GA-X99-Ultra-Gaming-rev-10/sp)
lists four physical x16-length PCIe 3.0 slots, with shared lanes. Several wide
cards need actual chassis/slot/cable clearance, not just a connector count.
NVIDIA gives reference graphics power of 300 W per 5070 Ti and 250 W per 5070;
PSU sizing must include the other installed cards and the rest of each node.
Upgraded fans/PSUs are planned, not verified installation. No five-GPU-in-one-node
assumption or specific PSU purchase recommendation follows.

## Concrete next work and evidence custody

Owner feedback is published and read back on
[DockingMT #33](https://github.com/uibcdf/dockingmt/issues/33#issuecomment-6772377034)
for the candidate serial CPU peptide profile and
[MolSysMT #558](https://github.com/uibcdf/molsysmt/issues/558#issuecomment-6772379174)
for conditional terminal-completion maps/history. The existing issues were
reused; no duplicate capability issue or external-author contact was created.
This feedback is a consumer need, not provider acceptance or a delivery promise.

1. Resolve the explicit molecular-profile choices in the linked preparation
   record through MolSysMT/DockingMT. Preserve read-only 1YCR as the reference.
2. Use existing DockingMT #33 for the owner disposition of a CPU HADDOCK3 peptide
   route and the cofolding-provider boundary. Receive source/binary/use terms and
   a bounded technical profile before any scientific sampling. No local adapter.
3. When the actual provider and scientific recipe are approved, measure a small
   serial CPU technical case first. A stopped run reports a resource/technical
   limitation; it is not evidence of biological failure or permission to enlarge
   resources. Fix sampling and acceptance before the proposed scientific pilot.
4. When a new GPU node is ready, inventory it, verify driver/framework/device
   identity and qualify one small fixed-input Boltz-2 case with an explicit new
   GPU/host-memory allocation. Other models and generators remain separate.

Evidence: [feasibility receipt](evidence/mdm2_node_feasibility_2026_11_10.json).
Full local outputs are retained under the receipt's task directory, including
hardware readings, inspected upstream source, raw coverage, both attempts and
the serial supervisor results. No T0 scientific geometry, HydrAMP or Macrel
checks were repeated. No docking, model/weights loading, GPU computation,
component installation, commit/push or package publication occurred. Existing
source profiles and concurrent sibling work were preserved. This preparation
does not complete D52 or accept the pilot's proposed geometric criterion.
