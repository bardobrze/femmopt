import optimizer
import nlopt
import utils
import plotter

from shutil import rmtree
from os import path

OUTPUT_FOLDER = "C:/Temp/Femmopt"

rmtree(OUTPUT_FOLDER, True)
 
nl_evals = optimizer.optimize(nlopt.LN_NELDERMEAD, "NelderMead", OUTPUT_FOLDER)
dl_evals = optimizer.optimize(nlopt.GN_DIRECT_L, "DirectL", OUTPUT_FOLDER)
 
utils.write_evallog(path.join(OUTPUT_FOLDER, 'NelderMead_eval.dat'), nl_evals)
utils.write_evallog(path.join(OUTPUT_FOLDER, 'DirectL_eval.dat'), dl_evals)

plotter.plot_searchpath(OUTPUT_FOLDER, "NelderMead_searchpath", nl_evals)
plotter.plot_searchpath(OUTPUT_FOLDER, "DirectL_searchpath", dl_evals)

plotter.plot_objectives(OUTPUT_FOLDER, "Objective", nl_evals, dl_evals)