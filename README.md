# MatchBallista Build Notes
## Video demo
Watch on YouTube

## Overview
I used [Blender3D](https://www.blender.org/) to modify [gsyan’s Micro Ballista Remix](https://www.thingiverse.com/thing:1532775) model to add a firing mechanism so that a match can be launched remotely from a Raspberry Pi.

## Print settings
Print all the files in the STL directory with the following settings:
```
Infill density: 30%
Layer height: 0.2mm
Speed: Standard
```

## Assembly
1. Push the tube all the way to the front of the frame’s track, then add a drop of super glue so the piece doesn’t move. This is where you’ll attach the striker strip to ignite the match.
2. Measure the specific matches you plan to launch, then use a Dremel to make a cut at the proper spot on the bottom of the track where the dime will block the nock from shooting forward.
3. Use the Dremel to make a cut on the base. Make sure it lines up with your previous cut when you place the frame on the base.
4. Super glue a dime into the cut you made on the base. Once you place the frame on top of the base, the dime should slightly insert into the cut on the frame, just enough to prevent the nock from moving.
5. Attach an [SG90 servo](https://www.amazon.com/Micro-Helicopter-Airplane-Remote-Control/dp/B072V529YD) to the side of the base. It should be positioned in such a way that when the `release.py` script is executed, the servo arm pushes the frame away from the base & dime enough to allow the nock to shoot forward.
6. Wire the servo to the GPIO pins of your Raspberry Pi. The pinout changes between models, so check the documentation for your specific RPi version.
7. Push the nock onto the frame’s track, load a rubber band through the hole on the nock, then attach each end of the rubber band to the slots on the frame. 
8. Wrap a rubber band around the rear end of the base and frame to keep the frame secure while firing.
9. You should now be able to load the ballista by pulling the nock back behind the frame’s cut, then pressing the frame onto the base until the dime blocks the nock.
10. To fire the ballista, SSH into your Raspberry Pi and run: `python3 scripts/release.py`