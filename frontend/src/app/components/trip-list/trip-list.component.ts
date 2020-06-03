import { Component, OnInit, OnDestroy } from '@angular/core';
import { TripService } from 'src/app/services/trip/trip.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-trip-list',
  templateUrl: './trip-list.component.html',
  styleUrls: ['./trip-list.component.css']
})
export class TripListComponent implements OnInit, OnDestroy {
  tripSubscription: Subscription;
  trips;

  constructor(private tripService: TripService) { }

  ngOnInit(): void {
    this.getTrips();
  }

  ngOnDestroy(): void {
    this.tripSubscription.unsubscribe();
  }

  getTrips(): void {
    this.tripSubscription = this.tripService.getAllTrips().subscribe(trips => {
      this.trips = trips;
    })
  }

}
