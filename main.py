import click
import os

from disk_driller.driller import DiskDriller


@click.command()
@click.argument('directory', default=os.getcwd())
def main(directory):
    speed = DiskDriller.drill(directory)

    print('Speed: {speed:.2f} MBs per second'.format(
        speed=speed
    ))
