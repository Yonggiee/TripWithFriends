import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormControl } from '@angular/forms';

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
    country: new FormControl('', Validators.required),
  });

  constructor() {}

  ngOnInit(): void {}
}
