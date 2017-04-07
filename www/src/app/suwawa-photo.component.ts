import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Member } from './member';
import { MemberService } from './member.service';

@Component({
  moduleId: module.id,
  selector: 'suwawa-photo',
  templateUrl: 'suwawa-photo.component.html',
  styleUrls: ['suwawa-photo.component.css'],
})
export class SuwawaPhotoComponent implements OnInit {
  photoUrls: string[][];
  loading: boolean;

  constructor(
      private memberService: MemberService,
      private location: Location
      ) {}

  ngOnInit(): void {
    this.loading = true;

    this.memberService.getSuwawaPhotos()
                      .subscribe(
                        urls => {
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