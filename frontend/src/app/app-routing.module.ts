import { NgModule } from '@angular/core'
import { Routes, RouterModule } from  '@angular/router';
import { TripListComponent } from './components/trip-list/trip-list.component';
import { UserLoginComponent } from './components/user-page/user-login/user-login.component';
import { UserSignUpComponent } from './components/user-page/user-sign-up/user-sign-up.component';

const routes: Routes = [
    { path: '', component: UserLoginComponent },
    { path: 'signup', component: UserSignUpComponent },
    { path: 'trips', component: TripListComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
export const routingComponents = [TripListComponent, UserLoginComponent]