import { Component, OnInit } from '@angular/core';
import { IntercomponentSignalerService } from 'src/app/services/intercomponent-signaler/intercomponent-signaler.service';

@Component({
  selector: 'app-menu-header',
  templateUrl: './menu-header.component.html',
  styleUrls: ['./menu-header.component.css']
})
export class MenuHeaderComponent implements OnInit {
  public isLogged: boolean = false;

  constructor(private loginNotiService: IntercomponentSignalerService) { }

  ngOnInit(): void {
    if (localStorage.hasOwnProperty('refreshToken')) {
      this.isLogged = true;
    }
    this.loginNotiService.loginNotiService
      .subscribe(isLogged => {
        this.isLogged = isLogged;
        this.ngOnInit();
    });
  }

}
