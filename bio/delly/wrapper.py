__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_ref=False, parse_memory=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


exclude = snakemake.input.get("exclude", "")
if exclude:
    exclude = f"-x {exclude}"


shell(
    "(OMP_NUM_THREADS={snakemake.threads} delly call"
    " -g {snakemake.input.ref}"
    " {exclude}"
    " {extra}"
    " {snakemake.input.alns} | "
    # Convert output to specified format
    "bcftools view"
    " {bcftools_opts}"
    ") {log}"
)
