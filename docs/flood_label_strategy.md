# Flood Label Strategy

## Primary Dataset

Aegis will initially use the Global Flood Database (GFD)
as the primary source of historical flood observations.

## Purpose

The flood observations will be used to create the target variable
for the initial supervised machine learning model.

## Target

- 0 = No observed flood event
- 1 = Observed flood event

## Flood Information

The dataset provides spatial information about observed flood extent
for historical flood events.

## Integration With Weather Data

Historical flood events will be temporally and spatially aligned
with weather and precipitation data.

The resulting training examples will contain weather conditions
before a flood event and a corresponding flood/no-flood label.

## Initial Prediction Task

Given recent weather conditions at a location, predict whether
a flood event is likely to occur within a defined future time window.

## Important Limitation

The Global Flood Database does not represent every flood that occurred.
Therefore, absence of an observed flood in the dataset should not
automatically be interpreted as proof that no flooding occurred.

This limitation will be considered during dataset construction
and model evaluation.