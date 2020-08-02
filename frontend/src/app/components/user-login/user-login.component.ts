import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Validators } from '@angular/forms';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {
  isLoggedIn = false;
  errors: string = "";

  loginForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', Validators.required),
  });

  constructor(private userService: UserService) {
    this.userService.loginErrorService.subscribe(errors => {
      this.errors = errors;
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    const loginDetails = this.loginForm.value;
    this.userService.login(loginDetails);
  }
}
