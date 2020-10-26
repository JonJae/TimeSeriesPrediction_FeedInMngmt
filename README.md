# Quadra - Prediction of Renewable Power Loss caused by Feed-in Management




## Description

The term feed-in management refers to the curtailment of power that is fed into the power grid (‘available power’) (‘available power’) in dependence of the power that is actually used by connected consumers or is being transferred on to other grid areas (‘consumed power’). Both of these values need to be in a perfect balance for every 15 minute interval to ensure grid stability. Against this background, especially renewable energy systems like wind turbines pose a big challenge, since by default by default the power from these systems is very volatile. 

The dataset contains data starting from 01/01/2018 to 26/08/2019 for a specific wind park (likely in northern Germany) (likely in northern Germany) and the grid it is connected to. Besides several meteorological parameters obtained from a numerical weather model, we are delivered the normed values for the available power (from the wind turbines of the park), the consumed power in the grid and as the resulting difference the lost power, that could not be fed in.

## Goal

In our capstone project, we will try to create a time series model that predictss the lost power for the next control interval(s)(s) in dependence of parameters in the past. This might be useful for energy traders as well as the people in charge of guaranteeing grid stability.