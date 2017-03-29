import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Params }   from '@angular/router';
import { Location }                 from '@angular/common';
import { Member } from './member';
import { MemberService } from './member.service';
import 'rxjs/add/operator/switchMap';

@Component({
  moduleId: module.id,
  selector: 'member-photo',
  templateUrl: 'member-photo.component.html',
  styleUrls: ['member-photo.component.css'],
})
export class MemberPhotoComponent implements OnInit {
  photoUrls: string[][];
  loading: boolean;

  constructor(
      private memberService: MemberService,
      private route: ActivatedRoute,
      private location: Location
      ) {}

  ngOnInit(): void {
    this.loading = true;
    this.route.params
    .switchMap((params: Params) => this.memberService.getMemberPhotos(params['name']))
    .subscribe(urls => {
      this.photoUrls = [];
      while(urls.length > 0) {
        let tmp: string[] = [];

        for (let i = 0; i < 4; i++) {
          let url = urls.shift();
          if (url) {
            tmp.push(url);
          }
        }

        this.photoUrls.push(tmp);
      }
      this.loading = false;
    });
  }

  goBack(): void {
    this.location.back();
  }
}
