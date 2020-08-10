import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user/user.service';
import { FormGroup, FormControl, Validators, ValidatorFn, ValidationErrors } from '@angular/forms';

@Component({
  selector: 'app-user-sign-up',
  templateUrl: './user-sign-up.component.html',
  styleUrls: ['./user-sign-up.component.css']
})
export class UserSignUpComponent implements OnInit {
  passwordMatchValidator: ValidatorFn = (control: FormGroup): ValidationErrors | null => {
    const password = control.get('password');
    const passwordConfirm = control.get('password_confirm');

    return password && passwordConfirm && password.value === passwordConfirm.value ? null : { notMatched : true };
  };
  errors: string = "";

  signUpForm = new FormGroup({
    name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', Validators.required),
    password_confirm: new FormControl('',),
  }, { validators: this.passwordMatchValidator });

  constructor(private userService: UserService) {
    this.userService.loginErrorService.subscribe(errors => {
      this.errors = errors;
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    const signUpDetails = this.signUpForm.value;
    this.errors = "";
    this.userService.signUp(signUpDetails);
  }

}
