import pstats

data = pstats.Stats("Del_14_Benchmarking/someprogram_results.cprof")
data.sort_stats("cumulative").print_stats("someprogram")
