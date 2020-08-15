import { NgModule } from '@angular/core'
import { Routes, RouterModule } from  '@angular/router';
import { TripListComponent } from './components/trip-page/trip-list/trip-list.component';
import { TripNewComponent } from './components/trip-page/trip-new/trip-new.component';
import { UserLoginComponent } from './components/user-page/user-login/user-login.component';
import { UserSignUpComponent } from './components/user-page/user-sign-up/user-sign-up.component';
import { UserSuccessComponent } from './components/user-page/user-success/user-success.component';

const routes: Routes = [
    { path: '', component: UserLoginComponent },
    { path: 'signup', component: UserSignUpComponent },
    { path: 'signup-success', component: UserSuccessComponent },
    { path: 'trips', component: TripListComponent },
    { path: 'trips/new', component: TripNewComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
export const routingComponents = [TripListComponent, UserLoginComponent,
    UserSignUpComponent, UserSuccessComponent, TripNewComponent]