# based on official jupyter image, modified for me
FROM jupyter/minimal-notebook

LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools && \
    apt-get install -y --no-install-recommends r-base r-recommended && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install --yes \
    'nomkl' \
    'ipywidgets=7.0*' \
    'pandas=0.19*' \
    'numexpr=2.6*' \
    'matplotlib=2.0*' \
    'scipy=0.19*' \
    'seaborn=0.7*' \
    'scikit-learn=0.18*' \
    'scikit-image=0.12*' \
    'sympy=1.0*' \
    'cython=0.25*' \
    'patsy=0.4*' \
    'statsmodels=0.8*' \
    'cloudpickle=0.2*' \
    'dill=0.2*' \
    'numba=0.31*' \
    'bokeh=0.12*' \
    'sqlalchemy=1.1*' \
    'hdf5=1.8.17' \
    'h5py=2.6*' \
    'vincent=0.4.*' \
    'beautifulsoup4=4.5.*' \
    'protobuf=3.*' \
    'xlrd' \
    'nb_conda' && \
    conda install --channel conda-forge --yes 'opencv ' && \
    conda clean -tipsy && \
    conda install --channel r r-essentials && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    fix-permissions $CONDA_DIR && \
    pip install notebook --upgrade --pre && \
    pip install rpy2 cython fortran-magic

# Install facets which does not have a pip or conda package at the moment
RUN cd /tmp && \
    git clone https://github.com/PAIR-code/facets.git && \
    cd facets && \
    jupyter nbextension install facets-dist/ --sys-prefix && \
    rm -rf facets && \
    fix-permissions $CONDA_DIR

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

USER $NB_USER

