import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Validators } from '@angular/forms';
import { UserService } from 'src/app/services/user/user.service';
import { IntercomponentSignalerService } from 'src/app/services/intercomponent-signaler/intercomponent-signaler.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {
  errors: string = "";

  loginForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', Validators.required),
  });

  constructor(private userService: UserService,
              private loginNotiService: IntercomponentSignalerService,
              private router: Router) {
    this.userService.loginErrorService.subscribe(errors => {
      this.errors = errors;
    });
    this.loginNotiService.loginNotiService
      .subscribe(isLogged => {
        if(isLogged == true) {
          this.router.navigate(['/trips']);
        }
      });
  }

  ngOnInit(): void {}

  onSubmit() {
    const loginDetails = this.loginForm.value;
    this.userService.login(loginDetails);
  }
}
