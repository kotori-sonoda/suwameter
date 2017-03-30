import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MemberListComponent }  from './member-list.component';
import { MemberPhotoComponent } from './member-photo.component';

const routes: Routes = [
  { path: '', redirectTo: '/members', pathMatch: 'full' },
  { path: 'members',  component: MemberListComponent },
  { path: 'photos/:name', component: MemberPhotoComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
