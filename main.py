from service import service
from database.db_setup import first_setup

servicer = service.service(True, 1)

def run():
    first_setup.run()


if __name__ == "__main__":
    servicer.whats_wrong()
    run()
    print("Done")
