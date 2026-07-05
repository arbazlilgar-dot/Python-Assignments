from django.core.management.base import BaseCommand
from booking.models import City, BusOperator, Route, Seat, BoardingPoint, DroppingPoint, Offer
from datetime import time


class Command(BaseCommand):
    help = 'Load sample data for RedBooking'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Cities
        cities_data = [
            ('Bengaluru', 'Karnataka'), ('Hyderabad', 'Telangana'), ('Mumbai', 'Maharashtra'),
            ('Pune', 'Maharashtra'), ('Delhi', 'Delhi'), ('Jaipur', 'Rajasthan'),
            ('Chennai', 'Tamil Nadu'), ('Ahmedabad', 'Gujarat'), ('Udaipur', 'Rajasthan'),
            ('Kolkata', 'West Bengal'), ('Bhubaneswar', 'Odisha'), ('Vijayawada', 'Andhra Pradesh'),
        ]
        cities = {}
        for name, state in cities_data:
            city, _ = City.objects.get_or_create(name=name, state=state)
            cities[name] = city

        # Operators
        operators_data = [
            ('VRL Travels', 'Volvo A/C Sleeper (2+1)', 4.6, '1.2k ratings'),
            ('SRS Travels', 'Mercedes Multi-axle A/C Sleeper', 4.8, '2.4k ratings'),
            ('Orange Tours & Travels', 'Scania A/C Seater', 4.4, '890 ratings'),
            ('Kallada G4', 'Volvo B11R Multi-axle A/C Sleeper', 4.7, '1.8k ratings'),
            ('Greenline Travels', 'A/C Sleeper (2+1)', 4.2, '540 ratings'),
            ('National Travels', 'Non-AC Seater (2+2)', 3.8, '320 ratings'),
            ('IntrCity SmartBus', 'Volvo Multi-axle A/C Sleeper', 4.5, '1.5k ratings'),
            ('Sharma Travels', 'A/C Seater (2+2)', 4.1, '410 ratings'),
            ('Zingbus Premium', 'Mercedes Benz A/C Sleeper · Lounge', 4.9, '3.1k ratings'),
            ('Rajdhani Travels', 'Non-AC Sleeper (2+1)', 3.9, '280 ratings'),
            ('Morning Star Travels', 'Volvo A/C Sleeper (2+1)', 4.3, '720 ratings'),
            ('Diwakar Travels', 'Scania Multi-axle A/C Sleeper', 4.6, '1.1k ratings'),
            ('KSRTC Express', 'Non-AC Seater (2+2)', 3.6, '510 ratings'),
            ('NueGo Electric', 'Electric A/C Sleeper · Premium', 4.8, '980 ratings'),
        ]
        operators = {}
        for name, bus_type, rating, total_ratings in operators_data:
            op, _ = BusOperator.objects.get_or_create(
                name=name,
                defaults={'bus_type': bus_type, 'rating': rating, 'total_ratings': total_ratings}
            )
            operators[name] = op

        # Routes (Bengaluru → Hyderabad)
        routes_data = [
            ('Bengaluru', 'Hyderabad', 'VRL Travels', time(22, 30), time(7, 45), 555, 'Non-stop', 1299, 12, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'SRS Travels', time(21, 0), time(7, 0), 600, '1 stop', 1599, 8, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'Orange Tours & Travels', time(23, 15), time(8, 0), 525, 'Non-stop', 999, 22, 'ac seater'),
            ('Bengaluru', 'Hyderabad', 'Kallada G4', time(20, 30), time(7, 0), 630, 'Non-stop', 1799, 4, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'Greenline Travels', time(22, 0), time(7, 30), 570, '1 stop', 1099, 18, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'National Travels', time(8, 0), time(18, 15), 615, '2 stops', 649, 28, 'nonac seater'),
            ('Bengaluru', 'Hyderabad', 'IntrCity SmartBus', time(19, 45), time(5, 30), 585, 'Non-stop', 1399, 15, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'Sharma Travels', time(14, 30), time(23, 30), 540, '1 stop', 899, 20, 'ac seater'),
            ('Bengaluru', 'Hyderabad', 'Zingbus Premium', time(21, 30), time(6, 45), 555, 'Non-stop', 1899, 3, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'Rajdhani Travels', time(5, 30), time(16, 30), 660, '2 stops', 749, 26, 'nonac sleeper'),
            ('Bengaluru', 'Hyderabad', 'Morning Star Travels', time(23, 45), time(8, 45), 540, 'Non-stop', 1199, 10, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'Diwakar Travels', time(11, 0), time(20, 30), 570, '1 stop', 1499, 7, 'ac sleeper'),
            ('Bengaluru', 'Hyderabad', 'KSRTC Express', time(6, 45), time(18, 15), 690, '3 stops', 599, 32, 'nonac seater'),
            ('Bengaluru', 'Hyderabad', 'NueGo Electric', time(22, 15), time(7, 0), 525, 'Non-stop', 2099, 5, 'ac sleeper'),
            # Additional popular routes
            ('Bengaluru', 'Chennai', 'VRL Travels', time(22, 0), time(4, 30), 390, 'Non-stop', 499, 30, 'ac sleeper'),
            ('Mumbai', 'Pune', 'SRS Travels', time(9, 0), time(12, 15), 195, 'Non-stop', 299, 40, 'ac seater'),
            ('Delhi', 'Jaipur', 'Sharma Travels', time(23, 0), time(4, 45), 345, '1 stop', 599, 25, 'ac sleeper'),
            ('Hyderabad', 'Vijayawada', 'Orange Tours & Travels', time(21, 0), time(1, 20), 260, 'Non-stop', 449, 35, 'ac sleeper'),
            ('Kolkata', 'Bhubaneswar', 'Greenline Travels', time(20, 0), time(3, 10), 430, '1 stop', 699, 20, 'ac sleeper'),
            ('Ahmedabad', 'Udaipur', 'Rajdhani Travels', time(22, 30), time(4, 0), 330, 'Non-stop', 549, 28, 'ac sleeper'),
        ]

        for from_name, to_name, op_name, dep, arr, dur, stops, price, seats_avail, tags in routes_data:
            route, created = Route.objects.get_or_create(
                from_city=cities[from_name],
                to_city=cities[to_name],
                operator=operators[op_name],
                departure_time=dep,
                defaults={
                    'arrival_time': arr, 'duration': dur, 'stops': stops,
                    'price': price, 'seats_available': seats_avail,
                    'bus_type_tags': tags,
                }
            )

            # Create seats for each route if new
            if created:
                # Lower deck: L1-L20
                lower_statuses = ['available'] * 20
                lower_statuses[2] = 'female'  # L3
                lower_statuses[8] = 'booked'   # L9
                lower_statuses[9] = 'booked'   # L10
                lower_statuses[15] = 'booked'  # L16

                for i in range(1, 21):
                    Seat.objects.create(
                        route=route,
                        seat_number=f'L{i}',
                        deck='lower',
                        status=lower_statuses[i-1],
                        tier='window' if (i % 4 in [1, 0]) else 'standard',
                        price=price + (100 if (i % 4 in [1, 0]) else 0),
                    )

                # Upper deck: U1-U12
                upper_statuses = ['available'] * 12
                upper_statuses[1] = 'booked'   # U2
                upper_statuses[7] = 'female'   # U8

                for i in range(1, 13):
                    Seat.objects.create(
                        route=route,
                        seat_number=f'U{i}',
                        deck='upper',
                        status=upper_statuses[i-1],
                        tier='premium' if i >= 9 else 'upper',
                        price=price + (300 if i >= 9 else 200),
                    )

                # Boarding points
                bp_data = [
                    ('Madiwala', 'BMTC Bus stop, near Hosur Rd', time(22, 0)),
                    ('Silk Board', 'Outer Ring Rd', time(22, 15)),
                    ('Electronic City', 'Toll plaza', time(22, 45)),
                    ('Majestic', 'KSRTC Bus stand', time(21, 30)),
                ]
                for name, addr, t in bp_data:
                    BoardingPoint.objects.create(route=route, name=name, address=addr, time=t)

                # Dropping points
                dp_data = [
                    ('Mehdipatnam', 'Bus stop', time(7, 0)),
                    ('Lakdikapul', 'Metro station', time(7, 20)),
                    ('Ameerpet', 'Hotel front', time(7, 40)),
                    ('Secunderabad', 'Railway station', time(8, 10)),
                ]
                for name, addr, t in dp_data:
                    DroppingPoint.objects.create(route=route, name=name, address=addr, time=t)

        # Offers
        offers_data = [
            ('Flat ₹250 off on first ride', 'FIRST250', 'Limited time', 'offer-1'),
            ('15% off on weekend trips', 'WKND15', 'Weekend', 'offer-2'),
            ('Up to ₹150 cashback', 'WALLET150', 'Wallet', 'offer-3'),
            ('20% off on AC sleepers', 'SLEEP20', 'Premium', 'offer-4'),
        ]
        for title, code, badge, color_class in offers_data:
            Offer.objects.get_or_create(code=code, defaults={'title': title, 'badge': badge, 'color_class': color_class})

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))
        self.stdout.write(f'  Cities: {City.objects.count()}')
        self.stdout.write(f'  Operators: {BusOperator.objects.count()}')
        self.stdout.write(f'  Routes: {Route.objects.count()}')
        self.stdout.write(f'  Seats: {Seat.objects.count()}')
        self.stdout.write(f'  Offers: {Offer.objects.count()}')
