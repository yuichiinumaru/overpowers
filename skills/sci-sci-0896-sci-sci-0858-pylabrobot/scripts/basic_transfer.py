#!/usr/bin/env python3
"""
Basic PyLabRobot script demonstrating a simulated liquid transfer protocol.
Useful as a starting template.
"""
import asyncio

try:
    from pylabrobot.liquid_handling import LiquidHandler
    from pylabrobot.liquid_handling.backends.simulation.simulator_backend import SimulatorBackend
    from pylabrobot.resources.hamilton import STARLetDeck
    from pylabrobot.resources.corning_costar import Cor_96_wellplate_360ul_Fb
    from pylabrobot.resources.hamilton import HTF_L

    # Check if visualization is requested
    import sys
    use_viz = "--viz" in sys.argv
    if use_viz:
        try:
            from pylabrobot.visualizer.visualizer import Visualizer
            print("Visualizer will be started at http://localhost:1337")
        except ImportError:
            print("Visualizer not installed. Proceeding without visualization.")
            use_viz = False

except ImportError as e:
    print(f"Error: Missing PyLabRobot dependencies: {e}")
    print("Run: uv pip install pylabrobot")
    sys.exit(1)

async def run_protocol():
    print("Initializing simulated liquid handler...")
    backend = SimulatorBackend()
    deck = STARLetDeck()
    lh = LiquidHandler(backend=backend, deck=deck)

    if use_viz:
        viz = Visualizer(lh)
        await viz.setup()

    await lh.setup()

    try:
        print("Setting up deck resources...")
        # Add tip rack and plates
        tip_rack = HTF_L(name="tips")
        source_plate = Cor_96_wellplate_360ul_Fb(name="source")
        dest_plate = Cor_96_wellplate_360ul_Fb(name="dest")

        # Assign to deck (coordinates/rails depend on specific deck)
        lh.deck.assign_child_resource(tip_rack, rails=1)
        lh.deck.assign_child_resource(source_plate, rails=10)
        lh.deck.assign_child_resource(dest_plate, rails=15)

        print("Executing transfer protocol...")
        # Simple transfer from column 1 of source to column 1 of dest
        await lh.pick_up_tips(tip_rack["A1:H1"])

        # Aspirate 50uL
        print("Aspirating...")
        await lh.aspirate(source_plate["A1:H1"], vols=50)

        # Dispense 50uL
        print("Dispensing...")
        await lh.dispense(dest_plate["A1:H1"], vols=50)

        print("Dropping tips...")
        await lh.drop_tips(tip_rack["A1:H1"])

        print("Protocol completed successfully!")

    finally:
        print("Stopping liquid handler...")
        await lh.stop()
        if use_viz:
            await viz.stop()

if __name__ == "__main__":
    asyncio.run(run_protocol())
