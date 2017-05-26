# 《机器学习基础：案例研究》 课程作业环境搭建

## 安装GraphLab Create
[GraphLab-Create](https://turi.com/download/install-graphlab-create-command-line.html)  
Step 1: Download Anaconda2 v4.0.0
Step 2: Install Anaconda

### Run Anaconda2 v4.0.0 installer.
bash /path to download file/Anaconda2-4.0.0-Linux-x86_64.sh
Step 3: Create conda environment

### Create a new conda environment with Python 2.7.x
conda create -n gl-env python=2.7 anaconda=4.0.0

### Activate the conda environment
source activate gl-env
Step 4: Ensure pip version >= 7

### Ensure pip is updated to the latest version
### miniconda users may need to install pip first, using 'conda install pip'
conda update pip
Step 5: Install GraphLab Create

### Install your licensed copy of GraphLab Create
pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/your registered email address here/your product key here/GraphLab-Create-License.tar.gz
Step 4: Ensure installation of IPython and IPython Notebook

### Install or update IPython and IPython Notebook
conda install ipython-notebook

## 安装 SFrame
[SFrame](https://github.com/turi-code/SFrame):  
pip install -U sframe
