# Add your constants here

# type 1 - direct

BASE_URL = "https://restful-booker.herokuapp.com"


# type 2 normal functions

def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


# Update :- PUT, PATCH, DELETE - we need a bookingId also

def url_patch_put_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking" + str(booking_id)


# type 3 - class functions

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # Update :- PUT, PATCH, DELETE - we need a bookingId also

    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(self.booking_id)
