import { NgModule } from '@angular/core'
import { Routes, RouterModule } from  '@angular/router';
import { TripListComponent } from './components/trip-list/trip-list.component';

const routes: Routes = [
    { path: '', component: TripListComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
export const routingComponents = [TripListComponent,]