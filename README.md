# codriver stages

Pace-note stages for [codriver](https://github.com/W0nt3x/codriver-for-forza-horizon-6),
the rally co-driver for Forza Horizon 6, shared by players. Install them from the
Stages tab inside codriver; no download needed.

## Contribute a stage

1. In codriver, record the race once and build it. Name it exactly like the race
   in Forza, for example `Coast Road Sprint`.
2. Drive it a few times and press **Learn** so the line and the speeds are good.
3. Press **Share** on the stage. codriver writes a clean file and opens this
   repository's upload page. Drag the file onto it and press *Propose changes*.
   GitHub turns that into a pull request.

Files go into `stages/`, named as a lowercase slug of the race name
(`coast-road-sprint.json`). One file per race; a better version of an existing
stage replaces the old file in a new pull request.

`index.json` is generated automatically after every merge; do not edit it.

## What a stage file contains

The recorded line (positions every 3 metres), the generated pace notes, the
settings that built it, and the slowest speed driven through each corner. It
contains no personal data and no telemetry recording; the recording stays on
the contributor's PC.
