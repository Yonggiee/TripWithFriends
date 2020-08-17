import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { baseurl, getHttpOptionsWithAuth, httpOptions } from '../commons.service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class TripService {
  errors: string = '';
  private errorSignal = new Subject<string>();
  public loginErrorService = this.errorSignal.asObservable();

  constructor(private http: HttpClient, private router: Router) {}

  getAllTrips(): Observable<any> {
    return this.http.get(baseurl + '/trips/', getHttpOptionsWithAuth());
  }

  postNewTrip(tripDetails): void {
    this.errors = '';
    this.http.post(baseurl + '/trips/', tripDetails, getHttpOptionsWithAuth()).subscribe(
      (response) => {
        this.router.navigate(['/trips']);
      },
      (err) => {
        const errors = err['error'];
        for (let key in errors) {
          this.errors += errors[key] + '\n';
        }
        console.log(this.errors);
        this.errorSignal.next(this.errors);
      }
    );
  }
}
