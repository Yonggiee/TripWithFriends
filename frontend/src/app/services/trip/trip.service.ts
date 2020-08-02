import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { baseurl, getHttpOptionsWithAuth } from '../commons.service';

@Injectable({
  providedIn: 'root'
})
export class TripService {

  constructor(private http: HttpClient) { }

  getAllTrips(): Observable<any> {
    return this.http.get(baseurl + '/trips/', getHttpOptionsWithAuth());
  }
}
