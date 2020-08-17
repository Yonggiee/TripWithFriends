import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormControl, FormArray } from '@angular/forms';
import { TripService } from 'src/app/services/trip/trip.service';

@Component({
  selector: 'app-trip-new',
  templateUrl: './trip-new.component.html',
  styleUrls: ['./trip-new.component.css'],
})
export class TripNewComponent implements OnInit {
  countries = [
    '',
    'Singapore',
    'Malaysia',
    'Thailand',
    'South Korea',
    'Japan',
    'UK',
    'USA',
    'China',
    'Vietnam',
    'Indonesia',
    'Myammar',
    'HongKong',
    'Others',
  ];

  tripForm = new FormGroup({
    name: new FormControl('', Validators.required),
    country: new FormControl(''),
    tags: new FormArray([new FormControl('')])
  });

  constructor(private tripService: TripService) {}

  ngOnInit(): void {}

  onSubmit() {
    const tripDetails = this.tripForm.value;
    console.log(tripDetails);
    this.tripService.postNewTrip(tripDetails);
  }

  addTagFormControl() {
    const tags = this.tripForm.get('tags') as FormArray
    tags.push(new FormControl(''));
  }
}
