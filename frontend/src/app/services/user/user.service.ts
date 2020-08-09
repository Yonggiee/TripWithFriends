import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { baseurl, httpOptions } from '../commons.service';
import { IntercomponentSignalerService } from '../intercomponent-signaler/intercomponent-signaler.service';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private errors: string = "";
  private errorSignal = new Subject<string>();
  public loginErrorService = this.errorSignal.asObservable();

  constructor(
    private http: HttpClient,
    private loginNotiService: IntercomponentSignalerService,
    private router: Router
  ) {}

  public login(loginDetails): void {
    this.errors = "";
    this.http
      .post(baseurl + '/api/token/', loginDetails, httpOptions)
      .subscribe(
        (data) => {
          this.updateAfterLogin(data);
          this.loginNotiService.triggerLoginService();
          this.router.navigate(['/trips']);
        },
        (err) => {
          this.errors = err['error']['detail'];
          this.errorSignal.next(this.errors);
        }
      );
  }

  signUp(signUpDetails): void {
    this.errors = "";
    this.http
      .post(baseurl + '/user/', signUpDetails, httpOptions)
      .subscribe(
        (response) => {
          this.router.navigate(['']);
        },
        (err) => {
          const errors = err['error'];
          for (let key in errors) {
            this.errors += errors[key] + "\n";
          }
          console.log(this.errors);
          this.errorSignal.next(this.errors);
        }
      );
  }

  public logout() {
    localStorage.clear();
    this.loginNotiService.triggerLoginService();
  }

  private updateAfterLogin(data): void {
    const accessToken = data['access'];
    const refreshToken = data['refresh'];
    this.updateAccess(accessToken);
    this.updateRefresh(refreshToken);
  }

  private updateAccess(token): void {
    localStorage.setItem('accessToken', token);
    this.errors = "";
  }

  private updateRefresh(token): void {
    localStorage.setItem('refreshToken', token);
    this.errors = "";
  }
}
