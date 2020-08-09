import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { MenuHeaderComponent } from './components/menu-header/menu-header.component';
import { ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule, routingComponents } from './app-routing.module';
import { UserLoginComponent } from './components/user-page/user-login/user-login.component';
import { UserSignUpComponent } from './components/user-page/user-sign-up/user-sign-up.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuHeaderComponent,
    routingComponents,
    UserLoginComponent,
    UserSignUpComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
