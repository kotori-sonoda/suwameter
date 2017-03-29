import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent }  from './app.component';
import { MemberListComponent } from './member-list.component';
import { MemberPhotoComponent } from './member-photo.component';
import { MemberService } from './member.service';

@NgModule({
  imports:      [
    BrowserModule,
    HttpModule,
    AppRoutingModule
    ],
  declarations: [
    AppComponent,
    MemberListComponent,
    MemberPhotoComponent
    ],
  providers:    [ MemberService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
