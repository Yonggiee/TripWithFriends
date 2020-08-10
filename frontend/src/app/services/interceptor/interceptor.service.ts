import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { catchError, flatMap } from 'rxjs/operators';
import { throwError } from 'rxjs'
import { baseurl, httpOptions } from '../commons.service';

@Injectable({
  providedIn: 'root'
})
export class InterceptorService implements HttpInterceptor{

  constructor(private http: HttpClient) { }

  intercept(req, next) {
    if (req.method == "POST") {
      return next.handle(this.addToken(req)).pipe(catchError(error => {
        if (error instanceof HttpErrorResponse && error.status === 401) {
          return this.handle401Error(req, next);
        }
        return throwError(error);
      }));
    }
    return next.handle(req);
  }

  handle401Error(req, next) {
    const refreshToken = localStorage.getItem('refreshToken');
    return this.http
      .post(
        baseurl + '/api/token/refresh/',
        JSON.stringify({ refresh: refreshToken }),
        httpOptions
      ).pipe(flatMap(
        (data) => {
          //If reload successful update tokens
          localStorage.setItem("accessToken", data['access']);
          //Clone our fieled request ant try to resend it
          return next.handle(this.addToken(req));
        }));
  }

  private addToken(req) {
    const accessToken = localStorage.getItem('accessToken');
    let httpOptionsWithToken = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + accessToken
    });
    let tokenisedReq = req.clone({
      headers: httpOptionsWithToken
    })
    return tokenisedReq;
  }
}
