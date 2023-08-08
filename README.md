# Time Series Decomposition Project

This project contains a Python script to retrieve a time series from an API and then decompose it into its observed, trend, seasonal, and residual components.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The script requires the following Python libraries:

* `requests`
* `pandas`
* `scipy`
* `statsmodels`
* `matplotlib`

You can install these using pip:

```sh
pip install requests pandas scipy statsmodels matplotlib
```

### Installing

To use the script, first clone the repository to your local machine:

```sh
git clone <https://github.com/ryanbvrns/EIA-Electricity-Price-Decomposition>
```

Then navigate to the cloned directory:

```sh
cd <EIA-Electricity-Price-Decomposition>
```

## Running the Script

Before running the script, you must replace `'API_Key_Here'` in the line `api_key = 'API_Key_Here'` with your actual API key for `api.eia.gov`.

You can then run the script using Python:

```sh
python EIA_Electricity_Price_Decomposition.py
```

This will print the decomposed time series components in four separate plots: observed, trend, seasonal, and residual.

## Code Explanation

The script uses the `requests` library to make an API call and get the time series data. This data is then cleaned and organized using `pandas`.

The `decompose_time_series()` function takes the organized time series data and decomposes it into its observed, trend, seasonal, and residual components using the `seasonal_decompose()` function from the `statsmodels.tsa.seasonal` library.

The decomposed components are then visualized using `matplotlib`.

## Authors

* Ryan Burns

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* This project was inspired by @kperry2215's work on
