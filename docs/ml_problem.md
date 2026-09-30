# Aegis Initial ML Problem

## Problem

Given recent weather and rainfall conditions in a geographic area,
predict whether a flood event is likely to occur within a future time window.

## Initial Task

Binary classification.

## Target

- 0 = No flood event
- 1 = Flood event

## Initial Features

Potential features include:

- Previous 24-hour rainfall
- Previous 72-hour rainfall
- Rainfall intensity
- Temperature
- Humidity
- Atmospheric pressure
- Wind conditions
- Elevation
- Historical flood frequency

## Initial Geographic Scope

A manageable geographic region will be selected for the first working model.

The system architecture will later support expansion to multiple regions
and eventually global coverage.

## Model Development Strategy

Several feature groups will be compared:

### Model A

Rainfall features only.

### Model B

Rainfall + weather features.

### Model C

Weather + geographic features.

### Model D

Weather + geographic features + historical flood information.

The models will be evaluated using metrics such as:

- Precision
- Recall
- F1-score
- PR-AUC

Accuracy alone will not be used as the main evaluation metric because
flood events may be much less frequent than non-flood events.

## Important Safety Note

Aegis is a decision-support system.

Its predictions do not replace official emergency warnings,
evacuation orders, or instructions from relevant authorities.