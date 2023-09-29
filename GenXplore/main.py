"""
Part of GenXplore software to process results of the GenX capacity expansion model.

Runs functions.

Written by:
Drew Kassel
Webber Energy Group

"""

# Import packages
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style

plt.style.use("default")
# plt.style.use("dark_background")

from warnings import simplefilter

from matplotlib.lines import Line2D

import GenXplore.settings as settings

settings.init()

from GenXplore.capacity_expansion import (
    capacity_by_type,
    capacity_by_type_per_scenario,
    capacity_by_type_plotter,
    spec_capacity_hbar_plotter,
    tot_capacity_plotter,
)
from GenXplore.costs import (
    cumulative_cost_diff_all_scenarios,
    cumulative_cost_difference_plotter,
)
from GenXplore.emissions import (
    cumulative_emissions_all_scenarios,
    cumulative_emissions_diff_plotter,
)
from GenXplore.energy_consumption import (
    dispatch_plot_builder,
    energy_consumed_by_type,
    energy_consumed_by_type_per_scenario,
    energy_consumed_by_type_plotter,
)
from GenXplore.transmission_expansion import capacity_by_line, flow_across_line

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
pd.options.mode.chained_assignment = None

# Run Functions

tot_cap = capacity_by_type()
# capacity_by_type_per_scenario(tot_cap)
# capacity_by_type_plotter(tot_cap)
tot_capacity_plotter(tot_cap)
# for i in range(len(settings.technologies)):
#     tech = settings.technologies[i]
#     spec_capacity_hbar_plotter(tech)

tot_energy = energy_consumed_by_type()
energy_consumed_by_type_per_scenario(tot_energy)
energy_consumed_by_type_plotter(tot_energy)
# dispatch_plot_builder()

capacity_by_line()

# scenarios_list = list(settings.scenarios_dict)
# scenarios = []
# for i in range(len(scenarios_list)):
#     if "0.0gw" not in scenarios_list[i]:
#         scenarios.append(scenarios_list[i])

# # scenarios = scenarios[1:3] + scenarios[4:6]
# for i in range(len(scenarios)):
#     flow_across_line(scenarios[i], "32")

# cost_diffs_df = cumulative_cost_diff_all_scenarios()
# cumulative_cost_difference_plotter(cost_diffs_df, list(settings.model_year.values())[0])

# emissions_df = cumulative_emissions_all_scenarios()
# cumulative_emissions_diff_plotter(emissions_df, list(settings.model_year.values())[0])
