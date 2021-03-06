#  Energy Efficiency Action through Education

Recommend using a virtual environment, as streamlit has a lot of dependencies.
Run the app with the following commands.
```
pip install -r /path/to/requirements.txt
streamlit run frontend.py
```
To communicate with the rasabot from the command line, go into the rasabot directory and execute the following commands.
```
rasa train (train chatbot)
rasa run actions (run in bg or another terminal)
rasa shell (interact with chatbot)
```

# Table to Eurostat

- Format
    - Link to eurostat
    - Name on eurostat
    - Unit of measurement
    - Possible specification of data type in case mulitple in dataset

- Emissions per capita
    - https://ec.europa.eu/eurostat/databrowser/view/t2020_rd300/default/table?lang=en
    - Greenhouse gas emissions per capita
    - Tonnes of CO2 equivalent per capita.

- Taxes
    - https://ec.europa.eu/eurostat/databrowser/view/t2020_rt300/default/table?lang=en
    - Energy taxes
    - Million euro

- Energy productivity
    - https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ep/default/table?lang=EN
    - Energy productivity
    - Euro per kilogram of oil equivalent

- Energy efficiency
    - https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_eff/default/table?lang=EN
    - Energy efficiency
    - Million tonnes of oil equivalent
    - Primary energy consumption (Europe 2020-2030) [PEC2020]

- Energy consumption 
    - https://ec.europa.eu/eurostat/databrowser/view/sdg_07_20/default/table?lang=EN
    - Final energy consumption in households per capita
    - Kilogram of oil equivalent

- Emissions by sector 
    - https://ec.europa.eu/eurostat/databrowser/view/env_air_gge/default/table?lang=EN
    - Greenhouse gas emissions by source sector
    - Thousand tonnes

