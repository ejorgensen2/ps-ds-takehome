## Pluralsight DS Take-Home Assessment
Completed by: EJ

### Setup instructions

1. `git clone` the repository.
2. Ensure poetry is installed and run the following from the repository directory to finish setting up:
3. `poetry shell`
4. `poetry install`

### Output Predictions

The notebook `ps_ds_takehome.ipynb` walks through my steps of data exploration, cleaning, modeling, feature importance analysis, and final predictions. By testing 4 different classifiers built in to Scikit Learn, I found the best classifier to be the Gradient Boosting Classifier. Predictions from that classifier are below:

| Index | age | weight | bmi | blood_pressure | insulin_test | liver_stress_test | cardio_stress_test | years_smoking | zeta_disease |
| ----- | --- | ------ | --- | -------------- | ------------ | ----------------- | ------------------ | ------------- | ------------ |
| 0	| 24	| 151	| 39.5	| 69	| 72	| 1.3968	| 56	| 4	| 1 |
| 1	| 27	| 179	| 35.5	| 89	| 156	| 1.6608	| 43	| 6	| 0 |
| 2	| 34	| 147	| 26.9	| 76	| 74	| 1.6958	| 53	| 2	| 0 |
| 3	| 35	| 206	| 32.4	| 73	| 127	| 1.4608	| 61	| 6	| 1 |
| 4	| 60	| 193	| 29.8	| 62	| 192	| 1.7798	| 65	| 9	| 0 |
| 5	| 45	| 120	| 36.5	| 108	| 50	| 1.2978	| 54	| 12	| 0 |
| 6	| 20	| 139	| 38.2	| 61	| 77	| 1.5818	| 68	| 3	| 0 |
| 7	| 23	| 137	| 31.2	| 70	| 73	| 1.4168	| 59	| 7	| 1 |
| 8	| 36	| 195	| 30.5	| 59	| 141	| 1.4498	| 59	| 6	| 1 |
| 9	| 19	| 193	| 25.8	| 84	| 66	| 1.7938	| 50	| 3	| 0 |
| 10	| 47	| 216	| 34.7	| 70	| 170	| 1.7238	| 58	| 7	| 1 |
| 11	| 40	| 200	| 30.4	| 69	| 128	| 1.3118	| 60	| 3	| 1 |
| 12	| 21	| 154	| 46.5	| 88	| 121	| 1.2498	| 68	| 4	| 0 |
| 13	| 52	| 196	| 31.3	| 90	| 167	| 1.9238	| 66	| 10	| 1 |
| 14	| 30	| 181	| 37.4	| 93	| 157	| 2.0508	| 80	| 5	| 0 |
| 15	| 46	| 213	| 26.5	| 70	| 133	| 1.4788	| 55	| 12	| 1 |
| 16	| 29	| 173	| 50.7	| 91	| 221	| 1.4878	| 83	| 3	| 0 |
| 17	| 36	| 202	| 42.8	| 72	| 273	| 1.8748	| 72	| 13	| 1 |
| 18	| 27	| 197	| 29.1	| 72	| 362	| 1.4298	| 69	| 4	| 1 |
| 19	| 44	| 184	| 33.9	| 104	| 141	| 1.3268	| 60	| 2	| 1 |