{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f6bdad71-dc6b-4626-a32d-306db5b32c1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Task-2 Completed ✓ Images saved: 3D_BMD.png, 3D_SFD.png\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Task-2 : 3D SFD & BMD of All Longitudinal Girders (Load Case 1)\n",
    "\"\"\"\n",
    "\n",
    "import importlib.util\n",
    "import numpy as np\n",
    "import xarray as xr\n",
    "import matplotlib.pyplot as plt\n",
    "from mpl_toolkits.mplot3d import Axes3D\n",
    "\n",
    "\n",
    "NC_PATH = r\"C:\\Users\\ADWAITH\\Desktop\\internship\\screening_task.nc\"\n",
    "NODE_PY = r\"C:\\Users\\ADWAITH\\Desktop\\internship\\node.py\"\n",
    "ELEMENT_PY = r\"C:\\Users\\ADWAITH\\Desktop\\internship\\element.py\"\n",
    "\n",
    "\n",
    "def load_dict(path, varname):\n",
    "    spec = importlib.util.spec_from_file_location(\"mod\", path)\n",
    "    m = importlib.util.module_from_spec(spec)\n",
    "    spec.loader.exec_module(m)\n",
    "    return getattr(m, varname)\n",
    "\n",
    "nodes = load_dict(NODE_PY, \"nodes\")\n",
    "members = load_dict(ELEMENT_PY, \"members\")\n",
    "\n",
    "\n",
    "ds = xr.open_dataset(NC_PATH, engine=\"netcdf4\")\n",
    "forces = ds[\"forces\"]\n",
    "\n",
    "Mz_i, Mz_j = \"Mz_i\", \"Mz_j\"\n",
    "Vy_i, Vy_j = \"Vy_i\", \"Vy_j\"\n",
    "\n",
    "\n",
    "girders = [\n",
    "    [17,26,35,44,53,62,71,80],\n",
    "    [16,27,36,45,54,63,72,81],\n",
    "    [15,28,37,46,55,64,73,82],\n",
    "    [14,29,38,47,56,65,74,83],\n",
    "    [13,30,39,48,57,66,75,84]\n",
    "]\n",
    "\n",
    "def plot_3d(title, comp_i, comp_j, outfile):\n",
    "    fig = plt.figure(figsize=(12,7))\n",
    "    ax = fig.add_subplot(111, projection='3d')\n",
    "\n",
    "    colors = ['b','orange','g','r','purple']\n",
    "\n",
    "    for idx, girder in enumerate(girders):\n",
    "        X, Y, Z = [], [], []\n",
    "\n",
    "        for elem in girder:\n",
    "            ni, nj = members[elem]\n",
    "            xi, yi, zi = nodes[ni]\n",
    "            xj, yj, zj = nodes[nj]\n",
    "\n",
    "            Vi = float(forces.sel(Element=elem, Component=comp_i))\n",
    "            Vj = float(forces.sel(Element=elem, Component=comp_j))\n",
    "\n",
    "            scale = 0.04\n",
    "\n",
    "            X.extend([xi, xj])\n",
    "            Z.extend([zi, zj])\n",
    "            Y.extend([yi + Vi*scale, yj + Vj*scale])\n",
    "\n",
    "        ax.plot(X, Y, Z, color=colors[idx], linewidth=2)\n",
    "\n",
    "    ax.set_xlabel(\"X (m)\")\n",
    "    ax.set_ylabel(\"Vertical Extrusion\")\n",
    "    ax.set_zlabel(\"Z (m)\")\n",
    "    ax.set_title(title)\n",
    "    ax.grid(True)\n",
    "    plt.tight_layout()\n",
    "    plt.savefig(outfile, dpi=300)\n",
    "    plt.close()\n",
    "\n",
    "plot_3d(\"3D Bending Moment Diagram (Mz) — Load Case 1\", Mz_i, Mz_j, \"3D_BMD.png\")\n",
    "plot_3d(\"3D Shear Force Diagram (Vy) — Load Case 1\", Vy_i, Vy_j, \"3D_SFD.png\")\n",
    "\n",
    "print(\"Task-2 Completed ✓ Images saved: 3D_BMD.png, 3D_SFD.png\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2157e9f8-e6e2-4bba-b3a0-c11e6e06d80b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
