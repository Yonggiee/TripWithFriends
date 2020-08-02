import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { baseurl, httpOptions } from '../commons.service';
import { IntercomponentSignalerService } from '../intercomponent-signaler/intercomponent-signaler.service';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  errors: string = "";
  private errorSignal = new Subject<string>();
  loginErrorService = this.errorSignal.asObservable();

  constructor(
    private http: HttpClient,
    private loginNotiService: IntercomponentSignalerService
  ) {}

  login(loginDetails): void {
    this.http
      .post(baseurl + '/api/token/', loginDetails, httpOptions)
      .subscribe(
        (data) => {
          this.updateAfterLogin(data);
          this.loginNotiService.triggerLoginService();
        },
        (err) => {
          this.errors = err['error']['detail'];
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
