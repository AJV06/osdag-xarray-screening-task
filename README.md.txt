

**Applicant:** Adwaith Jacob Vinoy  
**College:** Manipal Institute of Technology  

This repository contains the solution for the **Osdag Winter Internship 2025 – Xarray and PyPlot screening task**.



- `screening_task.nc` – NetCDF dataset containing internal forces for all elements.
- `node.py` – Node coordinates dictionary: `node_id -> [x, y, z]`.
- `element.py` – Element connectivity dictionary: `member_id -> [start_node, end_node]`.



Script: `task1_sfd_bmd.py`

- Reads the NetCDF dataset with Xarray.
- Extracts `Mz_i`, `Mz_j`, `Vy_i`, `Vy_j` for the central longitudinal girder  
  elements `[15, 24, 33, 42, 51, 60, 69, 78, 83]`.
- Uses node z-coordinates to build a continuous diagram.
- Saves:
  - `central_BMD.png`
  - `central_SFD.png`

Run:

```bash
python task1_sfd_bmd.py
