import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MemberListComponent }  from './member-list.component';
import { MemberPhotoComponent } from './member-photo.component';
import { SuwawaPhotoComponent } from './suwawa-photo.component';

const routes: Routes = [
  { path: '', redirectTo: '/members', pathMatch: 'full' },
  { path: 'members',  component: MemberListComponent },
  { path: 'photos/:name', component: MemberPhotoComponent },
  { path: 'suwawa', component: SuwawaPhotoComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
