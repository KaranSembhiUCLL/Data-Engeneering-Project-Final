# Validatieregels per Kolom

## Yellow Taxi Pipeline

### Mandatory Kolommen

| Kolom                   | Type     | Regel                                      | Actie |
| ----------------------- | -------- | ------------------------------------------ | ----- |
| `tpep_pickup_datetime`  | Datetime | Not null                                   | Drop  |
| `tpep_dropoff_datetime` | Datetime | Not null · na pickup                       | Drop  |
| `passenger_count`       | Integer  | Not null · 1–8                             | Drop  |
| `trip_distance`         | Float    | Not null · > 0                             | Drop  |
| `PULocationID`          | Integer  | Not null                                   | Drop  |
| `DOLocationID`          | Integer  | Not null                                   | Drop  |
| `payment_type`          | Integer  | Not null · waarde in {0, 1, 2, 3, 4, 5, 6} | Drop  |
| `fare_amount`           | Float    | Not null · >= 0                            | Drop  |
| `total_amount`          | Float    | Not null · >= 0                            | Drop  |

### Non-mandatory Kolommen

| Kolom                  | Regel               | Actie                   |
| ---------------------- | ------------------- | ----------------------- |
| `tip_amount`           | Aanwezig in dataset | —                       |
| `tolls_amount`         | Aanwezig in dataset | —                       |
| `extra`                | Aanwezig in dataset | —                       |
| `airport_fee`          | Aanwezig in dataset | —                       |
| `congestion_surcharge` | Aanwezig in dataset | —                       |
| `store_and_fwd_flag`   | Aanwezig in dataset | Verwijderd in Processor |
| `RatecodeID`           | Aanwezig in dataset | Verwijderd in Processor |
| `VendorId`             | Aanwezig in dataset | Verwijderd in Processor |

---

## Cars Pipeline

### Mandatory Kolommen

| Kolom        | Type    | Regel                                            | Actie |
| ------------ | ------- | ------------------------------------------------ | ----- |
| `car_id`     | Integer | Not null                                         | Drop  |
| `brand`      | String  | Not null · in geldige merkenlijst                | Drop  |
| `year`       | Integer | Not null · 1990–2025                             | Drop  |
| `mileage_km` | Float   | Not null · >= 0                                  | Drop  |
| `fuel_type`  | String  | Not null · in {Petrol, Diesel, Electric, Hybrid} | Drop  |
| `price_eur`  | Float   | Not null · > 0                                   | Drop  |

### Non-mandatory Kolommen

| Kolom          | Type    | Regel           | Actie bij null                | Actie bij ongeldig |
| -------------- | ------- | --------------- | ----------------------------- | ------------------ |
| `engine_cc`    | Integer | > 0             | Drop                          | Drop               |
| `horsepower`   | Integer | > 0             | Drop                          | Drop               |
| `num_doors`    | Integer | In {2, 3, 4, 5} | Drop                          | Drop               |
| `co2_g_per_km` | Float   | >= 0            | 0 (Electric) · Drop (anderen) | DROP               |
