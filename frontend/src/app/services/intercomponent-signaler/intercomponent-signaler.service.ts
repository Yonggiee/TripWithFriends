import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class IntercomponentSignalerService {
  private loginSignal = new Subject<boolean>();
  loginNotiService = this.loginSignal.asObservable();
  isLogged: boolean = false;

  constructor() { }

  triggerLoginService() {
    if (localStorage.hasOwnProperty('refreshToken')) {
      this.isLogged = true;
    } else {
      this.isLogged = false;
    }
    this.loginSignal.next(this.isLogged);
  }
}
